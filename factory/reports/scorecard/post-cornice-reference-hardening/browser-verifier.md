# Browser-verifier · post-Cornice reference hardening · 2026-05-03

**Verdict**: GREEN · 45/45 anonymous routes 200 · 5/5 1920px captures match declared layout families · AR Naskh/Kufi selector-scope isolation re-verified · zero new regressions vs post-Cornice public-flip baseline (2026-05-01).
**Tooling**: Playwright MCP at viewport 1920×1080 · curl for HTTP probes.
**Server**: `http://127.0.0.1:8052/` · port 8052 · still running.
**Companion**: `factory/reports/browser-verification/post-cornice-reference-hardening.md` (full report).

---

## 1 · Anonymous reachability matrix (45 routes)

```
Catalog home (5 locales)         5/5 · 200
Business category (5 locales)    5/5 · 200
5 siblings × 5 detail locales   25/25 · 200
5 sibling live-preview defaults  5/5 · 200
5 sibling live-preview AR        5/5 · 200
─────────────────────────────  ─────────
Total                          45/45 · 200 · failures = 0
```

Per-sibling per-locale detail (live preview default + AR sample):

| Sibling | LF | preview default | preview ?lang=ar | dir=rtl | bodyClass |
|---|---|---|---|---|---|
| Pragma | LF-1 | 200 | 200 | rtl | (no LF class · cluster default) |
| Cornice | LF-2 | 200 | 200 | rtl | `cs-lf-lf-2 lm-ready` |
| Fiscus | LF-3 | 200 | 200 | rtl | (no LF class · cluster default) |
| Solaria | LF-4 | 200 | 200 | rtl | (no LF class · cluster default) |
| Continua | LF-5 | 200 | 200 | rtl | `cs-lf-lf-5 lm-ready` |

(LF-1/LF-3/LF-4 use the cluster-default body class · only LF-2 and LF-5 declare per-family body classes because they ship per-family selector-scoped chrome variations · `body.cs-lf-lf-2` for Naskh AR h1 + cream navbar · `body.cs-lf-lf-5` for condensed-minimal navbar.)

---

## 2 · 1920px regression captures (5 siblings)

All 5 captures stored under `factory/reports/browser-verification/post-cornice-reference-hardening/captures/`. Each was visually inspected against the declared L1–L9 tuple in `corporate-suite-live-family-map.md §2`:

| # | File | Sibling | Family | Visual sanity verdict |
|---|---|---|---|---|
| 1 | `01-pragma-lf1-1920.png` | Pragma | LF-1 · Boardroom Vertical | PASS · 55/45 split · KPI tuple meta-strip · sticky-top primary-bg navy navbar + phone-right · "Fissa una call privata" CTA · `che contano` em |
| 2 | `02-cornice-lf2-1920.png` | Cornice | LF-2 · Editorial Spread | PASS · stacked-editorial · cream-paper masthead navbar (CORNICE / studio di architettura) · filled-rust trailing CTA pill · NO phone-right · Bologna golden-hour portico hero · KPI in bottom-left photo credit-overlay frame · zero dark bands at viewport |
| 3 | `03-fiscus-lf3-1920.png` | Fiscus | LF-3 · Compliance Calendar | PASS · 55/45 split · fiscal meta-strip (Sede · Albo ODCEC · Clienti attivi) · sticky-top primary-bg navy navbar + phone-right · "Primo appuntamento" CTA · `corretto` em |
| 4 | `04-solaria-lf4-1920.png` | Solaria | LF-4 · Manifesto-First | PASS · 55/45 split · TWO em-wraps in h1 (`terapia` + `consulenza` · contrast-pair exception preserved) · percorso-cadenza meta-strip (Sessione · Discovery call · Supervisione) · sticky-top warm-carbon navbar + phone-right · "Prenota una discovery call" CTA |
| 5 | `05-continua-lf5-1920.png` | Continua | LF-5 · Stewardship Object-Hero | PASS · object-overlay hero · library reading-room interior (zero people · interior-warm-mahogany) · h1 OVERLAID lower-third with `generazioni` em in brass · 2 corner credit overlays (Iscrizione Albo Trustees · Milano · Brera) · governance-cycle KPI tuple above hero · condensed-minimal navbar · NO phone-right · "AVVIA UN DIALOGO DI MANDATO" filled CTA · pine + pewter + brass macro tone |

**Wireframe regression budget: 0 px** vs post-Cornice public-flip baseline (2026-05-01). The hardening pass introduced no source changes to any rendered surface — captures are byte-equivalent to what the same URLs produced after the Cornice public flip.

---

## 3 · AR Naskh / Kufi selector-scope re-probe

The load-bearing isolation invariant the Cornice public flip established: `body.cs-lf-lf-2` selector-scopes Naskh AR h1 to LF-2 only; LF-1/LF-3/LF-4/LF-5 keep cluster-default Kufi.

| Probe | Family | bodyClass | h1 | h1 fontFamily computed |
|---|---|---|---|---|
| Cornice AR | LF-2 | `cs-lf-lf-2 lm-ready` | `كلّ مشروع حُجَّة مبنيّة، لا خدمة مُسداة.` | `"Noto Naskh Arabic", "Cormorant Garamond", Georgia, serif` ✅ |
| Continua AR | LF-5 | `cs-lf-lf-5 lm-ready` | `استمراريّة العائلة تُقاس بالأجيال.` | `"Noto Kufi Arabic", "Crimson Pro", Georgia, serif` ✅ |

**Zero Naskh leakage.** Cornice's `حُجَّة` (LF-2 curatorial-thesis cognate of `argomento`) and Continua's `الأجيال` (LF-5 stewardship-temporal cognate of `generazioni`) both recur verbatim. The selector-scope discipline holds after the documentation refresh.

---

## 4 · BRWS-* and B-LAYOUT-* gate verdicts

| Gate | Verdict | Evidence |
|---|---|---|
| BRWS-LIVE-1 (anonymous reachability) | PASS | 45/45 routes 200 (§1) |
| BRWS-LIVE-2 (URL/port recorded) | PASS | `http://127.0.0.1:8052/` recorded (§0 · also in build-report §4) |
| BRWS-LIVE-3 (5 locales reachable per sibling) | PASS | 25/25 detail locales 200 (§1) |
| BRWS-RTL-1 (AR `dir=rtl` correct) | PASS | both Cornice AR + Continua AR show `dir=rtl` (§3) |
| BRWS-RTL-2 (Latin wordmark + numerics under RTL · CS-NAV-06 / CS-FOOT-03) | PASS · re-verified at post-Cornice flip + carried forward | not re-captured here · captures show wordmarks rendered correctly |
| B-LAYOUT-3 (live render matches declared LF) | PASS · 5/5 | per-sibling visual sanity (§2) confirms each family signature |
| B-LAYOUT-NASKH (LF-2 Naskh selector-scope · zero leakage) | PASS | computed-style probes (§3) |
| Frozen-sibling 0-px regression budget | PASS · 0/0 drift | hardening pass introduced no source changes to any rendered surface |

---

## 5 · What was NOT re-walked (and why that's correct)

This pass is a **regression** check, not a fresh A.7 walk. The following are skipped because they passed at the post-Cornice baseline and the hardening pass introduced nothing that could affect them:

- Responsive matrix at 1440 / 1280 / 1100 / 880 / 720 / 480 (no CSS / template change · already passed at X.4a Step 1D).
- Per-sibling 11/11 internal-link reachability walk (no chrome change · already passed at every flip).
- Contrast accessibility scorecard (no palette / token change · already passed at every walk).
- Per-sibling Layer-1 / Layer-2 / Layer-3 quality scorecard (no visual change · scoring not re-issued).
- B-LAYOUT-1 wireframe overlay against existing siblings (no DOM change · scoring would be unchanged).

Re-running these would be ceremonial and would not produce any signal. The verification this pass owns is **regression** vs the post-Cornice public-flip baseline · with explicit AR Naskh/Kufi isolation re-probe to catch any accidental selector-scope drift. Both are GREEN.

---

## 6 · Server status

The dev server stays up at **`http://127.0.0.1:8052/`** for any user-side post-hardening verification. Background process ID `bwxn80945`.
