# Solaria · Pass B multilingual scorecard

**Phase**: X.4 Pass B · `20260426T1500Z`
**Branch**: `phase-x4-solaria-passB-multilingual`
**Verdict scope**: multilingual completion (4 added locales · IT preserved
verbatim from Pass A) · NO public flip · NO archetype edits · NO new archetypes.

## 1 · Overall verdict

**PASS** · 5 locales authored · voice anchor verbatim across all 5 ·
RTL Arabic working · zero overflow · zero banned phrases · 546/546
tests · 1 pre-existing W001 (Pragma) · 0 new W001s for Solaria.

## 2 · Per-axis scores (1 – 5 scale)

| Axis | Score | Reason |
|---|---|---|
| Voice anchor preservation (CS-EXEC-01) | 5/5 | Verbatim-in-translation across IT/EN/FR/ES/AR · italic em pattern preserved per locale |
| Voice register coherence per locale | 5/5 | EN HBR · FR vouvoiement · ES usted · AR formal MSA · all sober, no funnel |
| Visual / layout fit per locale | 5/5 | overflowPx=0 at 1440 + 390 · h1 wraps within floor · grid mirrors AR correctly |
| RTL Arabic behaviour | 5/5 | dir=rtl + Noto Kufi swap + nav/footer/grid mirrored + form fields RTL |
| Locale switcher honesty (D-068) | 5/5 | 5 pills exposed · IT no longer alone · AR pill carries dir=rtl |
| Banned-phrase scan (CS-EXEC-04) | 5/5 | 0 hits across all 5 locales |
| Premium identity preservation across locales | 5/5 | Same hero + KPI + leadership + cases · only language changes |
| Imagery coherence per locale | 4/5 | Same 6-URL Pexels pool across all 5 (deliberate scoping · curator pass deferred) |
| Inner-page coverage in walk | 3/5 | 4 inner-page samples instead of full 5×5 grid (acceptable for Pass B; will need full grid for Pass C) |
| Test cascade integrity | 5/5 | 546/546 · public-count gate held at 21 (tier still draft) |

**Average**: 4.7 / 5 · same band as Pass A (4.67) but with multilingual
coverage extended from 1 to 5 locales — the per-axis weighting is now
spread over 5x more surface and the average held.

## 3 · Cell-by-cell PASS/FAIL summary

| # | Cell | Status |
|---|---|---|
| 1 | IT home / 1440 / voice anchor | PASS |
| 2 | EN home / 1440 / voice anchor | PASS |
| 3 | FR home / 1440 / voice anchor | PASS |
| 4 | ES home / 1440 / voice anchor | PASS |
| 5 | AR home / 1440 / voice anchor + RTL | PASS |
| 6 | AR percorsi / 1440 / RTL grid | PASS |
| 7 | AR contatti / 1440 / RTL form | PASS |
| 8 | AR home / 390 / mobile RTL | PASS |
| 9 | EN percorsi / 1440 / LTR mirror | PASS |
| 10 | FR il-coach / 1440 / 5-step + values | PASS |
| 11 | Banned-phrase grep / 5 locales | PASS · 0 hits |
| 12 | manage.py check | PASS · 0 new W001 |
| 13 | Test suite | PASS · 546/546 |
| 14 | Locale-switcher pill count | PASS · 5 pills |
| 15 | Voice anchor verbatim per locale | PASS · 5/5 |

15/15 cells PASS · 0 blocking · 0 required-tier defects.

## 4 · Issues found · fixes applied

| # | Issue | Severity | Fix applied |
|---|---|---|---|
| — | None | — | First walk passed cleanly. No fixes needed. |

This is consistent with Pass A's identity baseline: the corporate-suite
chrome + the Pass-A IT-distinct identity holds intact across the four
added locales without per-locale touch-ups.

## 5 · Differentiation status

D-054 10-gate diff vs Pragma + Fiscus from Pass A continues to hold:

| Gate | Solaria | Pragma | Fiscus |
|---|---|---|---|
| Cluster | coaching | corporate boardroom | tax advisory |
| Voice anchor | "Coaching is not therapy and not consultancy." | "Where decisions that matter are made." | "The correct filing, not the clever trick." |
| Primary CTA per locale | discovery call (free, 20-30 min) | private boardroom call (NDA-ready) | initial consultation (45 min, partner-led) |
| Cluster credentials | ICF-PCC / EMCC / Co-Active | CONSOB / MBA | ODCEC / Cassazionista / Revisore Legale |
| Imagery direction | 1:1 coaching conversation | boardroom workshop | fiscal desk |
| Typography | Fraunces (humanist) | Merriweather (transitional) | IBM Plex Serif (contemporary) |
| Palette | warm carbon + ochre | navy + emerald | warm-neutral + blu-notte + gold |

The diff renders in every locale because every locale uses the same
hero photo, same palette, same typography, same KPI, same leadership
+ cases — only the *language of the strings* changes.

## 6 · Multilingual verdict

**Solaria multilingual completion = COMPLETE**. Solaria now matches
the multilingual standard established by every previously-good
corporate-suite sibling (Pragma · Fiscus) and the wider 5-locale
shipped templates (Vertex · Cardio · Gusto · Dermatologia · Chiara ·
Pixel · Bottega · Luxe · Sapore · Brace · Casa · Villa · Lex · Juris
· Salute · Benessere · Famiglia · Aura · Elevate).

The 5-locale parity gap that the alignment-reset §5 flagged ("Solaria
currently ships **one locale**: Italian only … the original goal
'multilingual behaviour like previous good templates' is **explicitly
not met yet**") is now **closed**.

## 7 · What is left for Pass C

Pass C is the public-flip cascade. Specifically:

1. Flip `tier` from `draft` to `published_live` (one-line change in
   `seed_templates.py`).
2. Update the public-count test (`apps/catalog/tests.py` ·
   `test_public_catalog_count_is_21` → `_is_22`) and the 5 cascading
   tests that count "published_live" templates.
3. Update the homepage trust counter to surface "22 templates"
   instead of "21".
4. Update discovery facets so Solaria appears in `?cluster=business`
   and in the "Coaching" sub-facet.
5. Walk Solaria as an anonymous visitor (no `?preview=1`) on at
   least 2 locales (recommend IT + AR for the demanding combination).

Pass C is held under separate user authorization. Pass B does not
include any of the above.
