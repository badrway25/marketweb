# Cornice · A.6 IT review-lock · Master scorecard

```yaml
phase:    A.6 review-lock (IT-only · pre-multilingual)
date:     2026-05-01
template: cornice-architettura
archetype: corporate-suite (5th sibling)
layout_family: LF-2 · Editorial Spread (1st LF-2 occupant)
```

## §1 · Panel scores

| Panel | Score | Floor | Verdict |
|---|---:|---:|---|
| build-report | 4.9 / 5 | 4.5 | PASS |
| style-critic | 4.85 / 5 | 4.5 | PASS |
| contrast-accessibility | 4.7 / 5 | 4.5 | PASS |
| responsive-auditor | 4.7 / 5 | 4.5 | PASS |
| browser-verifier | 4.85 / 5 | 4.5 | PASS |
| release-gatekeeper | 4.8 / 5 | 4.5 | PASS |
| **MEAN** | **4.80 / 5** | **4.5** | **PASS** |

A.5 mean was 4.65 / 5. A.6 mean lifts to **4.80 / 5** because
the three findings (F1 review-blocking founder mismatch, F2 LF-2
chrome consistency, F3 magazine-grid editorial rhythm) all
addressed surfaces that A.5 left at floor or near-floor — review-
locking those surfaces lifted the panels' verdicts measurably.

## §2 · Critical dimensions (intake §10)

The intake §10 listed 9 critical dimensions for an editorial-
architectural archetype. Re-bound on the post-fix render:

| Dimension | Score | Verdict |
|---|---:|---|
| Voice fidelity (`argomento` curatorial motif · 12 italic em surfaces) | 5.0 | PASS |
| Architectural-vocabulary register (Risk C-1) | 5.0 | PASS |
| Founder credibility (LF-2 L6 single-portrait · binding triple · post-F1 photo↔copy agreement) | 4.9 | PASS |
| Magazine-spread editorial weight (LF-2 L7 · post-F3 dominant hero photo) | 4.9 | PASS |
| Chrome polarity consistency (cream LF-2 nav · post-F2 across 9 pages) | 5.0 | PASS |
| LF-2 layout distinctness vs siblings (5-axis + L1-L9) | 5.0 | PASS |
| Whistleblowing footer compliance (D.lgs. 24/2023) | 4.7 | PASS |
| Responsive behavior (1440 → 480) | 4.7 | PASS |
| Contrast / accessibility (AA on body, AA-large on display) | 4.7 | PASS |
| **MEAN** | **4.88** | **PASS** |

A.5 critical-dimension mean was 4.83. A.6 lifts to **4.88**.

## §3 · Blocking findings

| Finding ID | Severity | Status |
|---|---|---|
| F1 founder gender mismatch | review-blocking | RESOLVED at A.6 |
| F2 LF-2 nav chrome on inner pages | high | RESOLVED at A.6 |
| F3 magazine-grid hero empty band | medium | RESOLVED at A.6 |

**3/3 findings resolved · 0/0 open.**

## §4 · Frozen sibling regression

| Sibling | LF | Pre-A6 baseline | Post-A6 render | Verdict |
|---|---|---|---|---|
| Pragma | LF-1 | navy nav · boardroom · emerald | navy nav · boardroom · emerald | NO REGRESSION |
| Fiscus | LF-3 | dark gray nav · desk · warm-neutral | same | NO REGRESSION |
| Solaria | LF-4 | warm-carbon nav · 1:1 · ocra | same | NO REGRESSION |
| Continua | LF-5 | pine nav · library · brass | same | NO REGRESSION |

**4/4 frozen siblings unchanged.**

## §5 · Distinctness verdict (post-fix)

| Pair | 5-axis | Layout-distinctness |
|---|---|---|
| Cornice vs Pragma | 5/5 | 9/9 |
| Cornice vs Fiscus | 5/5 | 9/9 |
| Cornice vs Solaria | 5/5 | 8/9 |
| Cornice vs Continua | 5/5 | 8/9 |

**5/5 vs every existing sibling.** L7 magazine-grid distinctness
STRENGTHENED by F3.

## §6 · Test suite

```
Ran 546 tests in 176.056s
FAILED (failures=1)
```

`test_medical_and_restaurant_templates_have_booking_flag` —
PRE-EXISTING failure (Continua-related), documented in v15
baseline. NOT introduced by A.6.

**545/546 PASS.**

## §7 · Lock verdict

**A.6 IT review-lock CLOSED.**

The Cornice IT draft is locked for human visual review at the
URL `http://127.0.0.1:8052/templates/business/cornice-architettura/preview/?preview=1`
on the staff session.

Next gate: **user-handshake on IT walk**.
- ON GO: workflow C (EN/FR/ES/AR + AR RTL)
- ON HOLD: A.7 narrow re-author or A.6b re-build
- Public flip: workflow D · post-multilingual · post-second-handshake
