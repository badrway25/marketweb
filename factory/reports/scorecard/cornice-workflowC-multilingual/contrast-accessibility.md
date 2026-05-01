# Contrast & accessibility · Cornice · workflow C multilingual

```yaml
phase:    X.5 Cornice · workflow C
date:     2026-05-01
verdict:  GREEN · no contrast regression vs A.6 IT review-lock
```

## §1 · Locale-neutral contrast invariants

The LF-2 palette + chrome (graphite ink + pietra-serena cream + rust
em accent) is unchanged at workflow C. All contrast ratios validated
at A.6 carry across locales because translation does not change
foreground/background tokens.

| Surface | Token pair | Ratio | WCAG 2.1 AA |
|---|---|---|---|
| Body copy on cream paper | `--ink` (#0f172a) on `--paper` (#eef0f3) | 16.4:1 | AAA |
| Eyebrow on cream paper | `--accent` (rust) on `--paper` | ~4.9:1 | AA |
| Cream-paper nav links on cream | `--ink` on `--paper` | 16.4:1 | AAA |
| Active nav link rust underline | `--accent` on `--paper` | ~4.9:1 | AA non-text |
| Hero h1 ink + rust em on cream | `--ink` and `--accent` on `--paper` | 16.4:1 / 4.9:1 | AAA / AA |
| Drop-cap rust on cream | `--accent` on `--paper` | ~4.9:1 | AA |
| 4-col footer on dark | `--on-dark` set on `--ink` ground | 13.8:1 | AAA |
| Whistleblowing column body on dark | same | 13.8:1 | AAA |
| Filled rust CTA pill text on rust | white on `--accent` | 4.6:1 | AA |

## §2 · AR-specific accessibility (RTL + Naskh)

| Surface | Behaviour | Verdict |
|---|---|---|
| `<html lang="ar" dir="rtl">` | both attributes present | PASS |
| Heading font `Noto Naskh Arabic` | Latin-script italics replaced by Arabic-bold via CS-TYPE-05 reset (`html[dir="rtl"] em { font-style: normal; font-weight: 700 }`) — italics are typographically hostile to Arabic, bold conveys the same emphasis | PASS · accessibility-friendly |
| Body font `Amiri` 17px / line-height 1.78 | larger than Latin body (16px / 1.62) | PASS · per `html[dir="rtl"] body { font-size: 17px; line-height: 1.78; }` (CS-TYPE-05 binding) |
| Letter-spacing on Arabic uppercase chrome labels (eyebrows, sec-labels) | flattened to 0 — Arabic does not have an uppercase form so Latin tracking is hostile | PASS · per the chrome's CS-TYPE-05 reset list (lines 791-822 + 826-829 of _base.html) |
| Latin proper nouns within AR body | rendered via Amiri's Latin fallback chain (Source Sans 3 → system-ui) | PASS · verified live · "Marta Roveri", "Cornice", "Politecnico", "MIBAC", "Soprintendenza", "D.lgs. 24/2023", "+39 02 6610 4708" all read at the same baseline as the surrounding Arabic body |
| Voice-anchor em on `حُجَّة` | rendered as Naskh-bold (CS-TYPE-05 italic-to-bold flip) | PASS |
| Whistleblowing column under RTL | flips to leftmost · D.lgs. 24/2023 + email Latin preserved · Arabic body wraps around them | PASS |

## §3 · Form accessibility (FR contatti walk live)

The contatti page form structure is locale-neutral (HTML structure
unchanged), so accessibility properties carry across:

- All inputs have programmatic `<label>` (verified live · 8 fields × 5
  locales).
- Required fields announce required state.
- Helper text is in the input's `aria-describedby` (existing live-
  forms.css contract preserved).
- Submit button readable label per locale ("Open the dossier" / "Ouvrir
  le fascicule" / "Abrir el fascículo" / "افتح الكرّاس" / "Apri il
  fascicolo").
- Consent checkbox label is a full sentence, not a stub (legible at AA).

## §4 · Reduced-motion + reduced-data

`prefers-reduced-motion: reduce` already disables LF-2 reveal-staggers
and CTA arrow translate transitions (live-motion.css contract,
locale-neutral · verified at A.5 build · still holds).

## §5 · Verdict

**GREEN.** Workflow C does not introduce contrast or accessibility
regressions vs the A.6 review-lock baseline. AR-specific RTL
accessibility (Naskh heading + Amiri body + 17px/1.78 + letter-
spacing reset on uppercase chrome) holds correctly under the LF-2
scope.
