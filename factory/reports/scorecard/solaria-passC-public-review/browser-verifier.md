# Solaria · Pass C · browser verifier

**Voice**: browser verifier. Pre-registers what was probed and what
came back. Cites the rubric the corporate-suite browser-rubric standard
defines.

**Reference rubric**: `factory/standards/corporate-suite-browser-rubric.md`.
**Auth used**: `solaria_qa_staff` · staff session via `/account/login/`
with `?preview=1` query string per D-055.
**Server**: `python manage.py runserver 127.0.0.1:8731 --noreload`.
**Run-ISO**: `20260427T1000Z`.

---

## 1 · The Pass-C-specific check

Pass C exists to legitimize the staff-preview review path. The
single-most-load-bearing browser check is therefore:

> **From the IT home opened with `?preview=1`, all 11 internal hrefs
> on the page must resolve to HTTP 200 in the same authenticated
> session.**

Result, fetched live in the browser:

```
solaria-coaching/?preview=1                        → 200
solaria-coaching/preview/?preview=1                → 200
solaria-coaching/preview/?lang=en&preview=1        → 200
solaria-coaching/preview/?lang=fr&preview=1        → 200
solaria-coaching/preview/?lang=es&preview=1        → 200
solaria-coaching/preview/?lang=ar&preview=1        → 200
business/?preview=1                                → 200
solaria-coaching/preview/il-coach/?preview=1       → 200
solaria-coaching/preview/percorsi/?preview=1       → 200
solaria-coaching/preview/casi/?preview=1           → 200
solaria-coaching/preview/contatti/?preview=1       → 200
```

11/11 → 200. **PASS.**

The same 11 hrefs were captured **before** the Pass C source edits
were applied; that pre-fix run returned 9 × 404 + 2 × 200 (only the IT
home itself and the marketplace bar's "studio successivo" link
worked). Pass C lifted the count from 2 → 11.

---

## 2 · Per-locale browser checkpoints

| Locale | dir | h1 | h1 font | overflowPx |
|---|---|---|---|---|
| it | ltr | "Il coaching non è terapia e non è consulenza." | Fraunces | 0 |
| en | ltr | "Coaching is not therapy, and not consultancy." | Fraunces | 0 |
| fr | ltr | "Le coaching n'est ni une thérapie, ni du conseil." | Fraunces | 0 |
| es | ltr | "El coaching no es terapia, ni es consultoría." | Fraunces | 0 |
| ar | rtl | "التدريب ليس علاجاً نفسياً، وليس استشارة." | Noto Kufi Arabic | 0 |

Voice anchor verbatim-in-translation across all 5 locales (CS-EXEC-01
F2). Same as Pass B; reproduced here to certify Pass C did not
silently re-route any page through a different content tree.

---

## 3 · Per-viewport responsive checkpoints

| Viewport | Locale | Surface | overflow | hamburger | Notes |
|---|---|---|---|---|---|
| 1440×900 | it | home | 0 | hidden | reveals forced opaque, lazy→eager |
| 1440×900 | en | home | 0 | hidden | reached via EN pill (not URL edit) |
| 1440×900 | fr | home | 0 | hidden | reached via FR pill |
| 1440×900 | es | home | 0 | hidden | reached via ES pill |
| 1440×900 | ar | home | 0 | hidden | dir=rtl; navDir=rtl |
| 1440×900 | ar | /percorsi/ | 0 | hidden | reached via in-page nav link |
| 1440×900 | ar | /contatti/ | 0 | hidden | reached via in-page nav link |
| 1024×800 | it | home | -15 | hidden | KPI band wraps to 2×2 |
| 390×844 | ar | home | -15 | **visible** | RTL hamburger drawer present |

(`overflow = scrollWidth - clientWidth` — `-15` is reserved scrollbar
gutter on Chrome/Windows; not a regression.)

---

## 4 · Tier-gate regression check (the can't-leak check)

Same authenticated session, omitting `?preview=1`:

```
GET /templates/business/solaria-coaching/preview/         → 404 ✓
GET /templates/business/solaria-coaching/                 → 404 ✓
GET /templates/business/solaria-coaching/preview/?preview=1 → 200 ✓
```

The fix only carries the flag forward when it was already explicitly
opted into. It does not relax the gate.

Anonymous (no cookies) probes:

```
GET /                                              → 200, "21+" still in body
GET /templates/business/                          → 200, no Solaria card
GET /templates/business/solaria-coaching/         → 404
GET /templates/business/solaria-coaching/preview/ → 404
```

Public catalog count remains 21 / 22. Public flip cascade is **not**
in flight.

---

## 5 · Recorded deviations from a "naïve eyeball" walk

Carried verbatim from Pass A/B (every Solaria pass uses the same set):

1. Reveal-targets `[data-lm="reveal"]` were forced opaque before each
   capture so the screenshots show the post-IntersectionObserver state
   (~200 ms after any scroll).
2. Lazy images forced `loading="eager"` so portraits and case-study
   thumbnails actually appear in captures.
3. 1.0 – 1.5 s wait between locale switches to give the Pexels CDN
   time to deliver imagery.

These deviations are content-equivalent (no fabrication, no
substitution) — the page would look identical to a real visitor after
a brief scroll and a brief CDN wait.

---

## 6 · What was NOT checked, intentionally

- **Anonymous public walk on Solaria.** Impossible while
  `tier=draft`. Calls for the public-flip cascade.
- **Full 5-locale × 5-page × 5-viewport matrix.** Pass B already
  exercised the locale × page matrix; Pass C narrows to AR for inner-
  page proofs because AR is the most likely place a navigation
  regression would surface visibly.
- **Pragma + Fiscus regression check.** Pass C edits the corporate-
  suite chrome they share. A spot-check is recorded in the gatekeeper
  panel; a deeper sweep is not warranted because the change is a
  strict no-op for `published_live` templates (their request shape
  never sets `staff_preview` to True).

---

## 7 · Verdict

**Browser-verifier: GREEN.** The Pass-C-specific check (11/11 internal
hrefs → 200 from staff session) holds. The Pass-B locale + viewport
matrix that was preserved holds. The tier-gate has not leaked. The
anonymous public-count cascade has not flipped. Pass C is verified
live, not just "tests pass and we hope."
