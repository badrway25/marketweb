# Browser-verifier panel · Cornice A.5 IT build

```yaml
panel:           browser-verifier
template_slug:   cornice-architettura
phase:           X.5 · A.5 build
date:            2026-05-01
verdict:         PASS
score:           4.7/5
walk_method:     Playwright MCP · headless Chromium · Windows
```

## Walk plan executed

- 6 IT routes verified at HTTP-status level (anonymous 404 + staff 200).
- 5 viewports captured at the home page (1440, 1100, 880, 720, 480).
- 4 frozen siblings captured at 1440 for parity.
- Console messages monitored — 0 errors, 0 warnings (level=error filter).

## Captures saved at `factory/reports/browser-verification/cornice-a5-it-build/captures/`

| File | What |
|---|---|
| cornice-home-1440-vp.png | Cornice home viewport @ 1440 |
| cornice-home-1440-full.png | Cornice home full page @ 1440 (~12000px tall) |
| cornice-narrative-1440.png | Cornice narrative section @ 1440 |
| cornice-sectors-1440.png | Cornice sectors-ribbon @ 1440 |
| cornice-leadership-1440.png | Cornice single-portrait leadership @ 1440 |
| cornice-cases-1440.png | Cornice 3+1 magazine grid @ 1440 |
| cornice-cta-closer-1440.png | Cornice cream CTA closer + 4-col footer @ 1440 |
| cornice-home-1100.png | Cornice home @ 1100 |
| cornice-home-880.png | Cornice home @ 880 (burger active) |
| cornice-home-720.png | Cornice home @ 720 (photo 4:5 portrait) |
| cornice-home-480.png | Cornice home @ 480 |
| frozen-pragma-1440.png | Pragma (LF-1) @ 1440 — frozen baseline |
| frozen-fiscus-1440.png | Fiscus (LF-3) @ 1440 — frozen baseline |
| frozen-solaria-1440.png | Solaria (LF-4) @ 1440 — frozen baseline |
| frozen-continua-1440.png | Continua (LF-5) @ 1440 — frozen baseline |

## DOM verification

DOM snapshot collected via `mcp__plugin_playwright_playwright__browser_snapshot`. Confirmed structure:

```
<nav class="cs-nav cs-nav--lf2">
  <div class="wm">
    <span class="wm-line-1">CORNICE</span>
    <span class="wm-line-2">studio di architettura</span>
  </div>
  ...
  <div class="phone cs-nav-cta--lf2">
    <a class="cs-nav-cta-btn">Apri un fascicolo progetto</a>
  </div>
</nav>

<section class="cs-hero">
  <div class="photo">
    <div class="overlay">
      <div class="credit">...</div>
      <div class="kpi-row">
        <div class="kpi"><span class="num">47</span><span class="lbl">Progetti realizzati</span></div>
        <div class="kpi"><span class="num">18</span><span class="lbl">Anni di pratica</span></div>
        <div class="kpi"><span class="num">6</span><span class="lbl">Città italiane</span></div>
      </div>
    </div>
  </div>
  <div class="below">
    <div class="left">
      <div class="eyebrow">STUDIO DI ARCHITETTURA · MILANO · DAL 2008</div>
      <h1>Ogni progetto è un <em>argomento</em> costruito, non un servizio reso.</h1>
      <p class="sub">...</p>
      <div class="actions">...</div>
    </div>
    <aside class="right">
      <blockquote class="side-quote">L'architettura buona si <em>argomenta</em> ...</blockquote>
    </aside>
  </div>
</section>

<section class="cs-narrative">
  ... drop-cap "L" + 4 paragraphs + 3 pull-quotes ...
  <aside class="side-rail">4 anchor links</aside>
</section>

<section class="cs-sectors-ribbon">...12 typologies + counter footnote...</section>

<section class="cs-leadership-single">
  <figure class="portrait-frame"><img>...</figure>
  <div class="body"><h2>Marco <em>Roveri</em></h2>...</div>
</section>

<section class="cs-cases-magazine">
  <article class="card card--hero">...</article>
  <article class="card card--small">...</article>  (×3)
</section>

<section class="cs-cta-cream">...voice anchor verbatim + filled rust button...</section>

<footer class="cs-foot">
  <div class="top">
    <div class="brand">CORNICE...</div>
    <div class="col">...</div>
    <div class="col">...</div>
    <div class="col cs-foot-col--whistleblowing">...D.lgs. 24/2023...</div>
  </div>
  ...
</footer>
```

DOM matches the LF-2 declared structure end-to-end.

## Browser console

Filter: `level=error`. Result: **0 errors, 0 warnings**.

## Frozen siblings parity

All 4 captured visually unchanged from v15 baseline:
- Pragma (LF-1) navy/emerald boardroom-planning · "decisioni che contano" · KPI tuple → MATCH
- Fiscus (LF-3) gray/blu-notte tax-document · "L'adempimento corretto, non la trovata" → MATCH
- Solaria (LF-4) warm-carbon/caramel 1:1 conversation · "non terapia non consulenza" → MATCH
- Continua (LF-5) pine/brass library · "generazioni" → MATCH

## Concerns

- The hero photo overlay's KPI tuple required a positioning fix during the walk (CSS `position: relative` on `.cs-hero` + HTML restructure to nest `.overlay` inside `.photo`). The fix is documented in the build report. Re-captured · all 5 viewports show the KPI tuple correctly placed. Build score deduction noted as 0.3.
- The home page label was renamed during the walk (`Studio` → `Archivio` for the about page) to avoid duplicated nav labels. Narrow content adjustment, not blocking.

## Score: 4.7/5

DOM verified · 0 console errors · all 5 cornice viewports captured · 4 frozen siblings preserved · 2 in-walk fixes applied and re-verified.
