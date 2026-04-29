# Template multilingual orchestrator prompt

**Use this prompt to roll a premium IT-only base template out to additional locales (typically EN/FR/ES/AR with RTL).**
Paste it verbatim at the start of a workflow C pass. Replace the bracketed `<…>` slots in §0. The single canonical example to triangulate against is the Solaria Pass B precedent (11/11 captures across 5 locales · 0 fixes mid-walk · `MEMORY.md → phase_x4_solaria_passB_multilingual.md`).

The trap of multilingual passes: they are not translation passes. They are identity-preservation passes performed in 4 additional languages while RTL re-flows half the layout in one of them. Treat them with the same rigour as the original build pass, not less.

---

## 0 · Run-time slots (fill before first turn)

```
template_slug:                 <existing IT template slug>
cluster:                       <cluster name>
current_tier:                  <draft | review-ready | published_live>
base_locale:                   it
target_locales:                <subset of [en, fr, es, ar]>
rtl_required:                  <YES if ar in target_locales · else NO>
voice_anchor_it:               "<verbatim IT sentence with the <em> tag>"
em_word_it:                    <the load-bearing word the brief named>
contrast_pair_anchor:          <YES | NO · YES only on Solaria-style two-em-wrap anchors>
report_root:                   factory/reports/<archetype>/<template_slug>/multilingual-<YYYY-MM-DD>/
```

---

## 1 · Pre-flight (before any translation starts · ~10 min)

You MUST verify all of the following before C.2 begins. Each one missing is a stop.

1. **IT walk on file ≤ 30 days old · PASS verdict.** No stale verdict, no rollout. Re-walk if expired (`BROWSER_QUALITY_GATE.md §3`).
2. **Voice anchor sentence captured verbatim** in the template's planner brief AT `factory/reports/<archetype>/<template_slug>/planner-brief.md §7`. The em-word is named explicitly. If not, this is workflow A on the brief first — abort and route there.
3. **Imagery pack is locale-agnostic.** No IT-specific text baked into images, no chalkboard menus in Italian inside hero photos. If a slot is locale-tied, swap it now (this is workflow A on imagery, not workflow C).
4. **For AR specifically:** the cluster's skin already supports `dir="rtl"` via logical properties. Test by toggling `<html dir="rtl">` on the IT live render — if anything breaks horizontally (paddings, alignments, heading order), the skin needs a workflow A pass on RTL readiness BEFORE this pass continues. Do not paper over RTL bugs in the translation phase.
5. **Cluster terminology guide identified** at `factory/cluster_blueprints/<cluster>.md` (or the cluster's authoritative terminology source). Credentials per locale, legal-row entries per locale, currency / date formats, register conventions.
6. **AR-specific font swap path is wired:** Noto Kufi Arabic for headings, Amiri for body, Latin wordmark + `.num` retained on Latin font (CS-TYPE-06 · CS-NAV-06 · CS-FOOT-03).
7. **Letter-spacing reset under RTL:** all `0.22em` uppercase tracking resets to 0 in `html[dir="rtl"]` (CS-TYPE-05).
8. **No hardcoded LTR-only spacing or directional CSS** anywhere in the skin (`margin-left`, `padding-right`, etc. — must be `margin-inline-start`, `padding-inline-end`, etc. CS-RESPONSIVE-08).

If any of (1)-(8) fails, document the gap in `<report_root>/preflight-stop.md` and stop. The corrective is upstream (workflow A on chrome OR brief OR imagery), not in this pass.

---

## 2 · Mandatory inputs

1. `design-orchestrator/TEMPLATE_FACTORY_MODEL.md §5` — workflow C canonical sequence.
2. `design-orchestrator/BROWSER_QUALITY_GATE.md §4` — per-locale walk requirement and the precedent bar.
3. `design-orchestrator/SKILL_USAGE_POLICY.md §2 "Multilingual rollout"` — Pro Max for typography pairings per locale; Impeccable NOT loaded for translation work.
4. The cluster's `factory/standards/<cluster>-design-standard.md` typography rules · imagery rules · navbar/footer rules.
5. The IT planner brief (especially §7 multilingual_intent) and the IT walk verdict.
6. Solaria Pass B as the operational precedent — the 11-capture, 0-mid-walk-fix bar (`MEMORY.md` pointer).

---

## 3 · The pass · workflow C steps

### C.1 · Pre-flight (orchestrator · ~10 min)

The eight checks in §1 above. Output: `<report_root>/preflight.md` with each check's result and the artefact path verifying it. If a check fails, the pass stops here.

### C.2 · Translate (copy-translation agent · per-locale · ~45-90 min total)

Inputs: IT locale tree · voice anchor verbatim · em-word · cluster terminology rules.
Outputs: one locale tree per target locale at the seed path the cluster expects. The voice anchor is preserved per the strategy below. A translation-diff report at `<report_root>/copy-<locale>.md` for each locale.

**Voice-anchor strategy (do not deviate without planner sign-off):**
- The IT anchor's load-bearing word (the em-word) has a single equivalent in each target language. The translator brief names it before translation starts.
- The em-wrap moves with the equivalent word; the rest of the sentence rephrases naturally.
- For contrast-pair anchors (`contrast_pair_anchor=YES`, e.g. Solaria's `terapia` × `consulenza`), both em-words translate independently and both wraps move.
- The anchor is identifiable in every locale at the live render. If a translator's choice loses the anchor's load-bearing emphasis on the equivalent word, reject the translation.

**Anti-patterns (refuse these):**
- Machine-translating the anchor without identifying the equivalent em-word.
- Choosing a different em-word in a target language because "it sounds better." The anchor is identity.
- Adding marketing flourishes in the target language ("Discover our…") that did not exist in the IT source. CS-EXEC-04 banlist applies in every locale.
- Inventing credentials per locale ("Bar Association of Milan-equivalent" — only the actual Albo translates; non-existent equivalents do not get fake credentials).
- Skipping the legal row per locale (P.IVA / privacy / cookie / whistleblowing where required).

**For AR specifically:**
- Translator brief includes the Kufi/Amiri swap and the Latin wordmark preservation. Translation is text-only; font swap is skin work, already wired in pre-flight.
- Right-to-left reading order is verified at every paragraph break — the AR translation reads naturally in RTL, not as English-with-Arabic-words.
- Numbers stay Latin where the cluster convention is Latin (`.num` class · CS-FOOT-03).

### C.3 · Build (template-builder · light · ~20-30 min)

Inputs: locale trees from C.2.
Outputs: locale trees seeded · `seed_templates.py` updated · CLI green · live URLs openable in every target locale at the cluster's path convention.

This is a light build — no skin changes (skin already supports the rollout per pre-flight check 4 and 8). If the build needs skin changes, stop: the pre-flight was wrong, the cluster needs a workflow A on RTL readiness.

Gate: the suite is green AND every locale URL renders without console errors AND the locale switcher (CS-NAV-03) shows the new locales as live links with correct `lang` and `dir` attributes.

### C.4 · Per-locale walks (browser-verifier · one walk per locale · ~30 min × N locales)

This is the cluster's ship gate, run once per locale.

**Each locale walk produces:**
- A rubric verdict at `<report_root>/walk-<locale>.md` (PASS · BORDERLINE · FAIL)
- 6-12 captures at `factory/reports/browser-verification/<template_slug>/<locale>/`, including hero · KPI band · CTA · footer · the section the cluster's standard most often regresses on
- Per-cell evidence (DOM snippets, computed styles where contrast is at issue)

**For AR walk specifically (the RTL parity walk):**
- Visual mirroring verified: navbar trailing CTA moves to the left, footer columns stack right-to-left, hero photo position swapped per the 55/45 split convention.
- Latin wordmark stays on Latin font (CS-NAV-06 · CS-FOOT-03).
- Logical properties working: no horizontal scroll, no overflow, no clipped focus rings.
- Letter-spacing on uppercase eyebrows is 0 (CS-TYPE-05 RTL reset), not 0.22em.
- `.num` numerics stay Latin (tabular alignment preserved).
- Reading direction tested on long paragraphs (about page · case detail).
- Locale switcher's AR link has `lang="ar" dir="rtl"`; English/Italian/French/Spanish links keep `lang=<code> dir="ltr"`.

**The bar:** the Solaria Pass B precedent — 11/11 captures PASS across 5 locales with 0 fixes mid-walk. If a walk has fixes mid-walk, the rollout is incomplete; close the walk, route the fix to workflow B (template-edit-orchestrator), then re-open this pass on the next locale.

**Gate:** the orchestrator does not approve the rollout until EVERY locale walk verdict is on file. Subset flips are acceptable (e.g. flip IT/EN/FR/ES while holding AR for one more pass) but ONLY if the held locale specifically failed and the others passed cleanly.

### C.5 · Aggregate (release-gatekeeper + orchestrator)

Inputs: pre-flight · all per-locale walks · all copy diffs · cluster scorecard with per-locale rows.
Output: `<report_root>/multilingual-summary.md` with:
- One row per locale: walk verdict · capture count · blocking findings · § deviations
- Anchor preservation confirmation per locale (the em-word's equivalent is on the load-bearing word in every target language)
- Pexels-only re-confirmation on every locale's live render (CS-IMG-SRC-01 still holds)
- AR-specific RTL parity confirmation (if AR was on the list)
- The flip-decision matrix: per-locale flip authorised or held

User-handshake artefact at `<report_root>/user-handshake.md`. The user signs ship-or-hold per locale.

---

## 4 · Stop conditions

The pass HALTS at any of these:

1. **Any pre-flight check (1)-(8) failed.** Fix upstream first. Do not "translate around" a stale walk or a non-RTL-ready skin.
2. **A translator picked a different em-word.** The anchor is identity; the wrong word is identity loss. Re-translate with the brief's em-word called out.
3. **A locale walk shows a `[BLOCKING]` finding.** Cannot flip that locale. May still flip the passing locales subset.
4. **AR walk shows RTL breakage.** Stop AR specifically; do not flip. Route to workflow A on chrome (the skin's logical-property compliance is the corrective).
5. **A translator added marketing copy or invented credentials.** Reject the translation; CS-EXEC-04 / CS-EXEC-03 apply to every locale.
6. **The locale switcher does not function on the live render** (lang/dir wrong, page does not change). CS-NAV-03 is `[BLOCKING]`. Route to workflow B on the chrome partial.
7. **A non-Pexels URL is on a target-locale render** that was not on the IT render. Cross-locale imagery substitution is forbidden (the pack is locale-agnostic; if it is not, pre-flight check 3 was wrong).
8. **The pass touched palette or skin.** This is no longer a multilingual pass. It is a workflow A on chrome, and it inherits A's gates.
9. **Less than 6 captures per locale at C.4.** The walk is incomplete. The Solaria Pass B bar is 11 captures; the floor is 6.

When you stop, write the stop into `<report_root>/stop-<date>.md`. Surface to user.

---

## 5 · What flat / generic translation looks like (refuse it)

The Solaria Pass B precedent worked because the translator preserved voice. Flat translation is the failure mode where the IT identity dissolves into language-specific marketing default.

**Refuse a translation if:**
- It reads like the cluster's English-language SaaS competitors. The cluster's voice is institutional / sensorial / clinical / editorial — never "Discover the difference," "Unlock your potential," "Learn more."
- The em-word's equivalent does not carry the same load-bearing meaning. Translator brief should call this out specifically.
- Credentials were translated into rough equivalents that do not exist (e.g. "Bar Association of Milan certified attorney" for Cassazionista — the term Cassazionista has no English equivalent and stays Cassazionista with a clarifying gloss).
- Date / currency / register flattened to American conventions on EN (`Lei` / `Vous` register equivalents matter; `you` does not always cover them).
- The voice anchor's emphasis structure was lost in transit. CS-TYPE-02 binds in every locale.
- The translator removed cultural specificity to "make it global." Cultural specificity is part of the identity; flattening it makes the locale generic.
- AR translation was machine-output passed through without a native review. The Solaria precedent had explicit AR verification; that is the bar.

A translation that closes the rollout but leaves the template generic in 4 of 5 locales is a worse outcome than IT-only at premium quality. It is acceptable to hold a locale.

---

## 6 · RTL-specific checklist (AR walk only)

Run this list against the AR live render. Each item is a separate cell in the walk verdict.

- [ ] `<html dir="rtl" lang="ar">` set
- [ ] Hero 55/45 split mirrored: serif h1 RIGHT, photo LEFT
- [ ] Navbar trailing CTA on LEFT
- [ ] Footer columns stacked right-to-left
- [ ] Locale switcher pill: AR link active, `lang="ar" dir="rtl"`; other links keep their LTR direction
- [ ] Latin wordmark unchanged (CS-NAV-06 · CS-FOOT-03)
- [ ] `.num` numerics stay Latin font, tabular alignment preserved
- [ ] Heading font swap to Noto Kufi Arabic working
- [ ] Body font swap to Amiri working
- [ ] Letter-spacing on uppercase eyebrows is 0 (RTL reset · CS-TYPE-05)
- [ ] No `margin-left` / `padding-right` artifacts (logical properties only · CS-RESPONSIVE-08)
- [ ] Reading direction natural at every paragraph break
- [ ] No horizontal scroll at any of the cluster viewports
- [ ] Focus-visible gold ring still appears on keyboard walk
- [ ] Voice anchor's em-wrap preserved on the equivalent AR word
- [ ] CTA copy is natural AR (not transliterated English)

If ANY box fails, AR does not flip. The rest of the locales may, per §C.5.

---

## 7 · Reporting cadence

- After C.1 pre-flight: 1 paragraph · all 8 checks PASS or specific gap surfaced.
- After C.2 (per locale): 1 paragraph · "EN translated · anchor preserved on `<word>` · credentials reviewed · diff at <path>."
- After C.3: 1 paragraph · build green · all locale URLs openable.
- After C.4 (per locale walk): 3-6 lines · verdict + capture count + per-cell summary.
- After C.5: the per-locale flip-decision matrix + user-handshake.

---

## 8 · Closing reminder

Multilingual rollouts are where premium templates either earn international gravitas or collapse into machine-translated marketing copy. The discipline is in the pre-flight (skin must already be RTL-ready), in the anchor preservation (the em-word travels), and in the per-locale walk (every locale earns its own ship signal). Solaria Pass B set the bar at 11/11 captures with 0 fixes mid-walk; that bar is the precedent and the floor. Do not negotiate it down because a calendar is tight.
