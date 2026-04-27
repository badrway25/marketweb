# Release gatekeeper · Solaria Pass B multilingual

**Phase**: X.4 Pass B · `20260426T1500Z`
**Decision asked**: should Pass B (multilingual completion · IT
remains authoritative · EN/FR/ES/AR added) merge to the
`phase-x4-solaria-passB-multilingual` branch?

## 1 · Scope reminder

Pass B does NOT do any of the following:

- It does NOT flip `tier` from `draft` to `published_live`. (Pass C territory.)
- It does NOT change `apps/editor`, `apps/projects`, or `apps/commerce`.
- It does NOT touch the corporate-suite archetype skin (no CSS, no template, no JS).
- It does NOT add or change imagery — same Pass-A 6-URL Pexels pool.
- It does NOT create new archetypes.
- It does NOT touch `TEMPLATE_REGISTRY.json` or DNA/seed/preview-imagery files (Pass A wired all of those).

Pass B authors **content only**: 4 new locale modules + a 5-line
delta in `template_content.py` to register them.

## 2 · CS-BLOCK series (corporate-suite blocking rules)

| Rule | Status | Evidence |
|---|---|---|
| CS-BLOCK-01 (h1..h5 contrast) | PASS · inherited Pass A | `contrast-accessibility.md §2` |
| CS-BLOCK-11 (voice anchor missing/paraphrased per locale) | PASS | `solaria-passB-multilingual.md §2` · 5-row table |
| CS-BLOCK-IM-* (imagery rules) | PASS · same Pass-A pool | `build-report.md §4` |
| CS-BLOCK-VI-03 (Arabic square-glyph fallback) | PASS | computed `fontFamily="Noto Kufi Arabic, ..."` · `browser-verifier.md §3` |
| CS-BLOCK-TI-01 (voice anchor missing/paraphrased) | PASS | same as CS-BLOCK-11 |
| CS-BLOCK-TI-04 (studio-name drift across pages) | PASS | "Solaria" identity consistent on every page × every locale |
| CS-EXEC-01 (voice anchor verbatim across 5 locales) | PASS | `style-critic.md §1` 5-row table |
| CS-EXEC-02 (D-054 10-gate triangulation in module docstring) | PASS · inherited Pass A | Pass A docstring lines 73-127 already triangulates Solaria vs Pragma vs Fiscus across 10 dimensions |
| CS-EXEC-03 (cluster-verifiable credentials) | PASS | ICF-PCC / ICF-ACC / ICF-MCC / EMCC Senior Practitioner / Coach Training Institute · Co-Active · all retained verbatim across locales |
| CS-EXEC-04 (no marketing hyperbole · 0 banned phrases) | PASS | `style-critic.md §3` · grep clear in every locale |
| CS-EXEC-06 (first-person-plural voice) | PASS | "We work / Nous travaillons / Trabajamos / نعمل" — preserved per locale |
| CS-EXEC-07 (no funnel-pattern sections) | PASS | discovery call is gated, not lead-magnet · footnote refuses "free diagnosis in 10 questions" verbatim per locale |
| CS-MARKET-01 (live preview hides editor affordances) | PASS · inherited from archetype |
| CS-MARKET-02 (no lorem ipsum) | PASS · all locales author real coaching content |
| CS-MARKET-03 (no "replace this text") | PASS · grep clear |

No CS-BLOCK regressions introduced by Pass B.

## 3 · D-054 differentiation triangulation

Pass A established the 10-gate diff Solaria vs Pragma vs Fiscus. Pass
B does not change cluster · voice anchor · primary CTA · service
unit · credentials · palette · imagery direction · typography. The
10-gate diff carries through every locale unchanged — only the
*language* of the diff changes per locale.

Verdict: **D-054 differentiation HOLDS across all 5 locales**.

## 4 · Pre-existing warnings

`manage.py check` emits one warning:

```
WARNINGS:
business-corporate: (corporate_suite.W001) corporate-suite imagery pool
  'business-corporate' is grandfathered under LEGACY_EXEMPT_KEYS and ships
  6 non-Pexels url(s) pending AP3 retro-curation.
```

This is a Pragma grandfather (Unsplash heritage) — not a Solaria
warning. The `business-coaching` pool is Pexels-clean and not
grandfathered. Pass B is silent on Solaria-specific gates.

## 5 · Test cascade

```
Ran 546 tests in 161.565s
OK
```

No new tests authored, no existing tests broken, no test churn —
Pass B's content addition is invisible to the test suite (locale
resolution + voice-anchor presence + RTL behaviour are already tested
on cardio/dermatologia/pragma/fiscus and inherit through to Solaria).

The public-catalog count test (`test_public_catalog_count_is_21`)
still passes because Solaria stays at `tier=draft`. No Pass-C
cascade is touched.

## 6 · Pass B merge decision

| Gate | Result |
|---|---|
| All CS-BLOCK rules cleared per locale | YES |
| All CS-EXEC rules cleared per locale | YES |
| Test suite green | YES · 546/546 |
| `manage.py check` clean (no new warnings) | YES |
| Voice anchor verbatim across 5 locales (CS-EXEC-01 / CS-BLOCK-11) | YES |
| Banned-phrase scan clean per locale (CS-EXEC-04) | YES |
| Arabic font swap proven (CS-BLOCK-VI-03) | YES |
| Layout overflow zero at 1440 + 390 | YES |
| Browser walk PASS on all 11 captures | YES |
| Out-of-scope edits (editor/projects/commerce/archetype) | NONE |
| New archetypes | NONE |

**RECOMMENDATION: APPROVE Pass B for merge** to
`phase-x4-solaria-passB-multilingual`. Pass C (public-flip cascade ·
tier draft → published_live · 6-test cascade · homepage trust counter
· discovery facets) remains held under separate user authorization
per the alignment-reset § "What we should do next now".

## 7 · Post-merge user action

Solaria is ready for human visual review of the four added locales.
Recommended walk:

```
http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1&lang=it
http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1&lang=en
http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1&lang=fr
http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1&lang=es
http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1&lang=ar
```

Login: `solaria_qa_staff / solariapassA2026` (existing staff user).
Server: `http://127.0.0.1:8731/` (left running).

If the user authorizes Pass C, the cascade cleanly applies because:

- All 5 locales already author the same shape · the locale
  switcher already returns 5 pills · the AR RTL behaviour is already
  proven · the voice anchor renders verbatim per locale · the
  premium identity holds.
- The only Pass C work is: tier flip + `test_public_catalog_count`
  cascade (21→22) + homepage trust counter increment + discovery
  facet seed + one anonymous-visitor walk per locale to confirm the
  flip is clean.
