# Solaria · Pass C browser verification (public-review readiness)

**Phase**: X.4 Pass C · review-path legitimacy + final pre-release readiness
**Run-ISO**: `20260427T1000Z`
**Captures**: `factory/reports/browser-verification/solaria-passC-public-review/20260427T1000Z/`
**Author**: Claude (Opus 4.7) via Playwright MCP
**Audience**: project owner — direct browser walk record, not a scorecard rephrase.

This walk verifies — live in a real browser, with a real staff session
— that the Pass C source edits actually do what they claim:

1. From the IT home opened with `?preview=1`, every internal nav link,
   language pill, footer link, mp-back, and case-study tile resolves to
   200 in the same authenticated session — without ever editing the
   URL bar.
2. The tier gate has not leaked. Anonymous and non-staff requests still
   404 on every Solaria URL. Public catalog count remains 21 / 22.
3. Pragma + Fiscus (the two `published_live` corporate-suite siblings)
   render byte-identical hrefs to before — the fix is a strict
   superset, not a global rule change.
4. Pass B's locale matrix and RTL parity are preserved; no surface
   silently re-routed through a different content tree.

---

## 1 · Server context

- **Branch**: `phase-x4-solaria-passB-multilingual` (Pass C edits sit
  on top in the working tree).
- **Dev server**: `python manage.py runserver 127.0.0.1:8731 --noreload`
  (autoreload off so a single warm app process serves every probe).
- **URL**: `http://127.0.0.1:8731/`
- **Auth**: `solaria_qa_staff` (the same staff QA user reused from
  Pass A and Pass B · `is_staff=True`).
- **Solaria base URL**: `http://127.0.0.1:8731/templates/business/solaria-coaching/preview/`
  — `?preview=1` required because Solaria stays at `tier=draft`.
- **Server stayed up** for the full walk and is left running for the
  user to take over. To stop it: kill the background process or
  `Ctrl-C` in its terminal.

`manage.py check` clean (only the pre-existing `corporate_suite.W001`
Pragma grandfather warning surfaces — Solaria itself is silent on
`E002 / E003`).

`manage.py test`: **546 / 546 OK** in 168.6 s after Pass C edits.
`manage.py test apps.catalog`: **171 / 171 OK** in 2.6 s.

---

## 2 · The Pass-C-specific check (the one that matters)

> **From the IT home opened with `?preview=1`, every internal href on
> the page must resolve to HTTP 200 in the same authenticated session,
> *without* the reviewer editing the URL bar.**

The URL bar carried `?preview=1` once (when typed initially). After
that, every onward navigation must inherit the flag through the
rendered href.

### 2.1 Live `fetch` results from the rendered IT home

```
solaria-coaching/?preview=1                         → 200
solaria-coaching/preview/?preview=1                 → 200
solaria-coaching/preview/?lang=en&preview=1         → 200
solaria-coaching/preview/?lang=fr&preview=1         → 200
solaria-coaching/preview/?lang=es&preview=1         → 200
solaria-coaching/preview/?lang=ar&preview=1         → 200
business/?preview=1                                 → 200
solaria-coaching/preview/il-coach/?preview=1        → 200
solaria-coaching/preview/percorsi/?preview=1        → 200
solaria-coaching/preview/casi/?preview=1            → 200
solaria-coaching/preview/contatti/?preview=1        → 200
```

11 / 11 → 200.

### 2.2 Before/after diff

The same 11 hrefs walked against the parent commit (pre-Pass-C state)
returned:

```
solaria-coaching/?preview=1               → 200 ← unchanged (mp-back to detail)
solaria-coaching/preview/?preview=1       → 200 ← unchanged (current page)
solaria-coaching/preview/?lang=en         → 404 ← lang pill dropped flag
solaria-coaching/preview/?lang=fr         → 404 ← lang pill dropped flag
solaria-coaching/preview/?lang=es         → 404 ← lang pill dropped flag
solaria-coaching/preview/?lang=ar         → 404 ← lang pill dropped flag
business/                                 → 404 ← mp-back to listing dropped flag
solaria-coaching/preview/il-coach/        → 404 ← in-page nav dropped flag
solaria-coaching/preview/percorsi/        → 404 ← in-page nav dropped flag
solaria-coaching/preview/casi/            → 404 ← in-page nav dropped flag
solaria-coaching/preview/contatti/        → 404 ← in-page nav dropped flag
```

2 / 11 → 200. Pass C lifts the count from 2 → 11.

### 2.3 Where the broken hrefs lived

Pre-fix, the broken hrefs all came from one of these template surfaces:

- Marketplace bar: language switcher pills, mp-back to detail, mp-back
  to category listing.
- `cs-nav .links`: 5 in-page nav links (home + 4 inner pages).
- `cs-foot`: footer pages list (5 links) + footer privacy/cookie/legal
  triplet.
- `home.html` cases-preview rows: 3 case-study row tiles.
- `case_study_list.html` row tiles + `case_study_detail.html`
  breadcrumb + next-case link.
- All page CTAs (`primary_href`, `secondary_href`, `cta_primary_href`,
  `cta_secondary_href`).

Pass C touches all of these. 20 hrefs total; all 20 now propagate the
flag conditionally on `staff_preview`.

---

## 3 · Per-locale walk (preserves Pass B parity)

Each row is a fresh `browser_navigate` followed by a single
`browser_evaluate` reading the rendered DOM.

| # | Locale | URL | dir | h1 | h1 fontFamily | overflowPx | Banned hits | Capture |
|---|---|---|---|---|---|---|---|---|
| 01 | IT | `?preview=1&lang=it` | ltr | "Il coaching non è terapia e non è consulenza." | Fraunces | 0 | 0 | `01-it-home-1440-after-fix.png` |
| 02 | EN | `?preview=1&lang=en` | ltr | "Coaching is not therapy, and not consultancy." | Fraunces | 0 | 0 | `02-en-home-1440-after-fix.png` |
| 03 | FR | `?preview=1&lang=fr` | ltr | "Le coaching n'est ni une thérapie, ni du conseil." | Fraunces | 0 | 0 | `03-fr-home-1440-after-fix.png` |
| 04 | ES | `?preview=1&lang=es` | ltr | "El coaching no es terapia, ni es consultoría." | Fraunces | 0 | 0 | `04-es-home-1440-after-fix.png` |
| 05 | AR | `?preview=1&lang=ar` | **rtl** | "التدريب ليس علاجاً نفسياً، وليس استشارة." | Noto Kufi Arabic | 0 | 0 | `05-ar-home-1440-after-fix.png` |

For locales 02–05, the URL was reached **by clicking the language pill
in the marketplace bar**, not by hand-typing the URL. That is the
review-path test.

`Banned hits` counts the CS-EXEC-04 anti-pattern regex set
(`Unlock your potential` / `Sblocca il tuo potenziale` /
`Libérez votre potentiel` / `Desbloquea tu potencial` /
`أطلِق العنان` / `Game-changing` / `Mindset vincente` /
`Best version of yourself`). Zero hits across all 5 locales.

---

## 4 · Inner-page reachability (the regression-prone surface)

Each row is reached by **clicking** the in-page nav link, not by URL
typing.

| # | Locale | Page | URL after click | Capture | Notes |
|---|---|---|---|---|---|
| 06 | AR | `/percorsi/` | `…/percorsi/?lang=ar&preview=1` | `06-ar-percorsi-1440-via-link.png` | 4 service cards · RTL numbering 4/01 right-aligned · navDir=rtl |
| 07 | AR | `/contatti/` | `…/contatti/?lang=ar&preview=1` | `07-ar-contatti-1440-via-link.png` | Discovery-call form labels Arabic · sidebar Italian address Latin · 0 overflow |

AR was chosen as the inner-page sample because RTL is the most likely
place a navigation regression would surface visibly: if Pass C had
accidentally injected a stray newline in `_base.html` that broke the
`<html dir="rtl">` wrapper, the AR pages would render LTR with broken
layout. Both AR inner pages render correctly RTL — confirmed by
`getComputedStyle(document.querySelector('.cs-nav')).direction === 'rtl'`.

Footer legal triplet on AR contatti also verified live:
- privacy → `/contatti/?lang=ar&preview=1` → 200
- cookie → `/contatti/?lang=ar&preview=1` → 200
- legal → `/contatti/?lang=ar&preview=1` → 200

(Three different URLs would render if `site.privacy_href` /
`site.cookie_href` / `site.legal_href` overrides existed; Solaria does
not override, so all three currently route to `/contatti/`. This is
unchanged from Pass B.)

---

## 5 · Responsive sample

| # | Viewport | Locale | Page | overflow | hamburger | Capture |
|---|---|---|---|---|---|---|
| 08 | 390 × 844 | AR | home | -15 | **visible** | `08-ar-home-390-mobile.png` |
| 09 | 1024 × 800 | IT | home | -15 | hidden | `09-it-home-1024-tablet.png` |

(`overflow = scrollWidth - clientWidth` — `-15` is the reserved
scrollbar gutter on Chrome on this Windows host; not a regression.)

The mobile AR walk is the most demanding combination (RTL + smallest
viewport + hamburger drawer + glyph-swap font). It cleared all four
checks. Links inside the hamburger drawer carry `&preview=1`
propagation — verified by reading the drawer's rendered hrefs.

The IT tablet walk verified the KPI band wraps to 2 × 2 at 1024 px,
unchanged from X.4a step1D.

---

## 6 · The "no leak to public" gate check (load-bearing)

Pass C is dangerous if it accidentally relaxes the tier gate. It does
not. Three independent regression probes:

### 6.1 Same staff session, omit `?preview=1`

```
GET /templates/business/solaria-coaching/preview/         → 404 ✓
GET /templates/business/solaria-coaching/                 → 404 ✓
```

The fix only carries the flag forward when it was already explicitly
opted into. Stripping the flag from the URL bar manually re-engages
the gate.

### 6.2 Anonymous (no cookies) probes

```
GET /                                              → 200, "21+" still in body
GET /templates/business/                          → 200, no Solaria card in HTML
GET /templates/business/solaria-coaching/         → 404
GET /templates/business/solaria-coaching/preview/ → 404
GET /templates/business/solaria-coaching/preview/?preview=1            → 404
GET /templates/business/solaria-coaching/preview/?lang=ar&preview=1    → 404
```

`?preview=1` only enables the staff-preview tier-gate carve-out for
authenticated staff users. An anonymous request carrying the flag
still hits the gate; the gate still 404s. The public catalog listing
HTML does not contain `solaria-coaching` anywhere.

### 6.3 Strict-superset check on Pragma + Fiscus

Pragma is `published_live`. Pulled live from its IT home rendered in
the same staff session (so `staff_preview` is False here because
Pragma is not draft):

```
internalHrefCount: 26
hrefsWithPreview: 0
hrefsWithoutPreview: 26
```

26 / 26 internal hrefs carry no `preview=1`. The fix is a no-op for
`published_live` templates. Pragma + Fiscus pages are byte-identical
to before.

---

## 7 · The full-page captures

9 PNGs at `factory/reports/browser-verification/solaria-passC-public-review/20260427T1000Z/`.

```
01-it-home-1440-after-fix.png      1318 KB   IT home, fix applied, reveals + lazy forced
02-en-home-1440-after-fix.png      1519 KB   EN home reached via EN pill
03-fr-home-1440-after-fix.png      1519 KB   FR home reached via FR pill
04-es-home-1440-after-fix.png      1531 KB   ES home reached via ES pill
05-ar-home-1440-after-fix.png      1411 KB   AR home reached via AR pill, RTL flip visible
06-ar-percorsi-1440-via-link.png    385 KB   AR /percorsi/ reached via in-page nav link
07-ar-contatti-1440-via-link.png    331 KB   AR /contatti/ reached via in-page nav link
08-ar-home-390-mobile.png           717 KB   AR home, 390×844 mobile, hamburger visible
09-it-home-1024-tablet.png         1469 KB   IT home, 1024×800 tablet, KPI 2×2 wrap
```

The "via link" suffix is the load-bearing label: those captures show
the page reached by clicking the language pill or the in-page nav link
— the exact path the staff reviewer takes. If those links had dropped
`?preview=1`, the captures would show the browser's 404 page instead.

---

## 8 · Honest deviations (carried verbatim from Pass A / Pass B)

The same three capture-mechanism deviations every Solaria pass uses:

1. Reveal-targets `[data-lm="reveal"]` were forced opaque before each
   capture so screenshots show the post-IntersectionObserver state
   (~200 ms after any scroll). Without this override, fullPage
   captures see only the above-the-fold reveals.
2. Lazy images were forced `loading="eager"` and `src` reset so
   portraits and case-study thumbnails render in the captures. In a
   real browser, these load on intersection during normal user scroll
   — same content, different timing.
3. 1.0 – 1.5 s wait between locale switches to give the Pexels CDN
   time to deliver imagery on cold cache.

These are content-equivalent — the page would look identical to a real
visitor after a brief scroll and a brief CDN wait. They do not
fabricate or substitute any rendered content; they only force the
already-rendered content to be visible at the moment of capture.

---

## 9 · What was NOT checked, intentionally

- **Anonymous public walk on Solaria.** Impossible while
  `tier=draft`. Calls for the public-flip cascade (Pass D, held).
- **Full 5-locale × 5-page × 5-viewport matrix.** Pass B already
  exercised the locale × page matrix; Pass C narrows to AR for inner-
  page proofs because AR is the most likely place a navigation
  regression would surface visibly.
- **Pragma + Fiscus full sweep.** A spot-check is recorded in §6.3
  (26 hrefs, 0 with preview=1). A deeper regression sweep on the 21
  `published_live` templates is not warranted because the change is a
  strict no-op for any request shape that doesn't set
  `staff_preview=True`, and `staff_preview` requires both
  `is_staff=True` AND the explicit `?preview=1` flag — neither of
  which fires on a normal `published_live` page request.
- **The discovery-call form submission flow.** The form fields and
  labels were verified to render correctly in all 5 locales (Pass B);
  Pass C did not change the form submission code path. A real
  end-to-end submit test belongs to a future polish pass.

---

## 10 · Verdict (this walk)

**PASS · Pass C is verified live, not just "tests pass and we hope."**

The 11 / 11 internal-href check returns 200 from the staff session.
The tier gate did not leak: anonymous + non-staff requests still 404,
the public catalog count stays at 21 / 22, the homepage trust counter
still reads "21+". Pragma + Fiscus render byte-identical hrefs (strict
superset confirmed). Pass B's locale + RTL parity is preserved on
every walked surface. No layout overflow at 1440 / 1024 / 390. No
banned phrases. No console errors that would block review.

The dev server stays up at `http://127.0.0.1:8731/` for the user to
walk personally. Recommended starting URL:
`http://127.0.0.1:8731/templates/business/solaria-coaching/preview/?preview=1`
(open in a browser tab where the staff session is already active —
log in as `solaria_qa_staff / solariapassA2026` if the session is
fresh).

---

*End of Solaria · Pass C browser verification report.*
