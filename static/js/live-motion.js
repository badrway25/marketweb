/* ============================================================================
 * MarketWeb — Live Motion Language (pilot)
 * ============================================================================
 *
 * Minimal, dependency-free motion runtime for live_templates/<category>/
 * <archetype> skins. Pairs with static/css/live-motion.css.
 *
 * Responsibilities
 *   1. Arm the hidden state — only add `lm-ready` to <body> once we're ready
 *      to observe. If JS fails to load, the CSS hidden states never activate
 *      and the page renders in full (no blank hero).
 *   2. Observe `[data-lm="reveal|reveal-lg|reveal-soft"]` — add `.lm-in` once
 *      the element crosses the viewport threshold, then unobserve it (one-shot
 *      reveal, no re-trigger).
 *   3. Observe `[data-lm-stagger]` parents — when a parent intersects, assign
 *      a per-child `transition-delay` based on its index and the stagger
 *      unit, then add `.lm-in` on the parent so CSS reveals the children.
 *   4. Observe `[data-lm="counter"]` — on first intersect, animate the
 *      numeric prefix of the element's text from 0 to `data-lm-to`, preserving
 *      any non-numeric suffix (e.g. "180€").
 *   5. Respect `prefers-reduced-motion: reduce` — short-circuits to a plain
 *      render, skipping all observers and counters.
 *   6. Duplicate the `[data-lm="marquee"]` track once, so the CSS loop keyframe
 *      can translate it -50% and create a seamless scroll.
 *
 * This module is safe to load `defer` — it runs on DOMContentLoaded and does
 * nothing until the DOM is ready.
 *
 * Scope
 *   Loaded only inside live-template standalone skins. Do NOT load on the
 *   marketplace catalog surface (which has its own main.js).
 * ============================================================================ */

(function () {
  'use strict';

  var STAGGER_MS = 70;        // per-child delay in a staggered parent
  var REVEAL_THRESHOLD = 0.15;
  var ROOT_MARGIN = '0px 0px -80px 0px';
  var COUNTER_DURATION_MS = 1400;

  function init() {
    var body = document.body;
    if (!body) return;

    // Reduced motion: the user has asked us not to animate. Render everything
    // as-is and exit. We still add `lm-ready` so the CSS hidden-state gate is
    // technically "armed", but we also add `lm-reduced` which short-circuits
    // every transition in CSS.
    var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reducedMotion) {
      body.classList.add('lm-ready', 'lm-reduced');
      // Phase X.7d Causa retrofit slice 02 · EVID-3 reduced-motion fallback.
      // Open every `<details data-evid3>` on init so the citation snippets
      // ship as static "[collapse]" content per F2-VAR-1's reduced-motion
      // contract. The full-motion init() path leaves them in the native
      // closed state so the click-to-expand interaction reads correctly.
      document.querySelectorAll('details[data-evid3]').forEach(function (d) { d.open = true; });
      return;
    }

    // No IntersectionObserver? Fail open — render everything visible without
    // scroll gates. Shipping as-if-motion-off is better than broken layouts.
    if (!('IntersectionObserver' in window)) {
      body.classList.add('lm-ready');
      document.querySelectorAll('[data-lm]').forEach(function (el) { el.classList.add('lm-in'); });
      document.querySelectorAll('[data-lm-stagger]').forEach(function (el) { el.classList.add('lm-in'); });
      return;
    }

    body.classList.add('lm-ready');

    normalizeAliases();
    setupReveals();
    setupStaggers();
    setupCounters();
    setupMarquees();
    setupNavCondense();
    setupTime3();
  }

  // --- 0. Alias normalization --------------------------------------------------
  // Some archetypes (street-modern / Brace) were authored with `data-reveal`
  // and `data-stagger` shorthand. Normalize them to the canonical `data-lm`
  // contract so reveals + cascade fades actually fire. Idempotent.
  function normalizeAliases() {
    document.querySelectorAll('[data-reveal]').forEach(function (el) {
      if (!el.hasAttribute('data-lm')) el.setAttribute('data-lm', 'reveal');
      el.removeAttribute('data-reveal');
    });
    // Children marked `data-stagger` → lift to parent as `data-lm-stagger`,
    // then strip the child marker so the stagger CSS targets the correct level.
    document.querySelectorAll('[data-stagger]').forEach(function (el) {
      var parent = el.parentElement;
      if (parent && !parent.hasAttribute('data-lm-stagger')) {
        parent.setAttribute('data-lm-stagger', '');
      }
      el.removeAttribute('data-stagger');
    });
  }

  // --- 1. Reveals -----------------------------------------------------------
  function setupReveals() {
    var targets = document.querySelectorAll('[data-lm="reveal"], [data-lm="reveal-lg"], [data-lm="reveal-soft"]');
    if (!targets.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('lm-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: REVEAL_THRESHOLD, rootMargin: ROOT_MARGIN });

    targets.forEach(function (el) { io.observe(el); });
  }

  // --- 2. Staggered parents -------------------------------------------------
  function setupStaggers() {
    var parents = document.querySelectorAll('[data-lm-stagger]');
    if (!parents.length) return;

    parents.forEach(function (parent) {
      var unit = parseInt(parent.getAttribute('data-lm-stagger-delay'), 10) || STAGGER_MS;
      var base = parseInt(parent.getAttribute('data-lm-stagger-base'), 10) || 0;
      var children = parent.children;
      for (var i = 0; i < children.length; i++) {
        // Only the opacity/transform transition gets a delay; nothing else.
        children[i].style.transitionDelay = (base + i * unit) + 'ms';
      }
    });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('lm-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: REVEAL_THRESHOLD, rootMargin: ROOT_MARGIN });

    parents.forEach(function (el) { io.observe(el); });
  }

  // --- 3. Counters ----------------------------------------------------------
  function setupCounters() {
    // Phase X.7d slice 01 · counter activation gate. The `data-lm="counter"`
    // token is now a structural signal that does NOT drive animation by
    // itself; activation is gated by the per-template `motion_profile`,
    // propagated through `<body data-motion-kpi-animate="1">`. Templates
    // whose motion gravity opts out (G2-editorial · G4-stewardship · G6-
    // cinematic) ship without the attribute, the counter pass is skipped,
    // and KPI numbers render statically — same final value, zero animation.
    // The mapping from gravity to `kpi_animate` flag lives in
    // `apps/catalog/template_dna.py · MOTION_PROFILES`. (Body data-
    // attributes preferred over class names so the body-class shape stays
    // available to other systems · per `_base.html` body class contract.)
    if (document.body.getAttribute('data-motion-kpi-animate') !== '1') return;

    var counters = document.querySelectorAll('[data-lm="counter"]');
    if (!counters.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });

    counters.forEach(function (el) { io.observe(el); });
  }

  function animateCounter(el) {
    var original = (el.getAttribute('data-lm-original') || el.innerText || '').trim();
    // Parse OPTIONAL leading non-digit prefix + numeric portion + suffix
    // ("180€", "1.4k", "€ 1.4 B", "+ 38%", "↑ 22"). Prefix and suffix are
    // preserved verbatim — only the numeric span animates.
    var match = original.match(/^(\D*?)(-?\d+(?:[.,]\d+)?)(.*)$/);
    if (!match) return;

    var prefix = match[1] || '';
    var suffix = match[3] || '';

    var rawNum = el.getAttribute('data-lm-to') || match[2];

    // Thousand-separator heuristic — supports IT/DE/ES (dot) and EN/FR (comma
    // in some cases, though FR often uses narrow-space; comma is safer for
    // the stock Western-European registers we target). A value like "28.000"
    // or "28,000" (≥ 3-digit trailing group) is treated as a thousand-
    // separated integer; "1.4" or "1,4" stays a decimal (4-group would be
    // thousand-sep; single-digit/double-digit trailing group is decimal).
    var thousandsDot   = /^\d{1,3}(\.\d{3})+$/.exec(rawNum);
    var thousandsComma = /^\d{1,3}(,\d{3})+$/.exec(rawNum);
    var target;
    var thousandsSep = null;
    if (thousandsDot) {
      target = parseInt(rawNum.replace(/\./g, ''), 10);
      thousandsSep = '.';
    } else if (thousandsComma) {
      target = parseInt(rawNum.replace(/,/g, ''), 10);
      thousandsSep = ',';
    } else {
      // Treat comma as decimal separator when not in thousand-sep shape.
      target = parseFloat(String(rawNum).replace(',', '.'));
    }

    var isInt = thousandsSep ? true : (String(target).indexOf('.') === -1);
    var decimals = isInt ? 0 : (String(target).split('.')[1] || '').length;

    if (isNaN(target)) return;

    // Cache the pristine text so we never double-animate on re-observation.
    el.setAttribute('data-lm-original', original);

    var start = performance.now();
    function ease(t) { return 1 - Math.pow(1 - t, 3); } // easeOutCubic

    function formatValue(v) {
      if (isInt) {
        var n = Math.round(v);
        // Restore the original thousand-separator character so the animating
        // count keeps the locale convention we parsed.
        if (thousandsSep) {
          return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, thousandsSep);
        }
        return String(n);
      }
      return v.toFixed(decimals);
    }

    function frame(now) {
      var t = Math.min(1, (now - start) / COUNTER_DURATION_MS);
      var value = target * ease(t);
      el.innerText = prefix + formatValue(value) + suffix;
      if (t < 1) requestAnimationFrame(frame);
      else el.innerText = prefix + formatValue(target) + suffix;
    }
    requestAnimationFrame(frame);
  }

  // --- 3b. Nav condense-on-scroll ------------------------------------------
  // Phase X.7d Causa retrofit slice 01 · NAV-1 sticky-condensed pattern.
  // Profile-gated via `body[data-motion-nav-condense="1"]`; templates
  // whose motion gravity opts out (every profile except `g2-editorial-
  // counter` today) ship without the attribute and the listener is a
  // no-op. Hysteresis thresholds 240/80 prevent flicker around the
  // shrink boundary. Reduced-motion is already short-circuited at
  // `init()` above; this function won't run when `lm-reduced` is set.
  // CSS transition lives in corporate-suite/_base.html under
  // `body[data-motion-nav-condense="1"] .cs-nav.cs-nav--lf2.is-shrunk`.
  function setupNavCondense() {
    if (document.body.getAttribute('data-motion-nav-condense') !== '1') return;
    var nav = document.querySelector('nav.cs-nav');
    if (!nav) return;

    var SHRINK_AT = 240;
    var GROW_AT = 80;
    var ticking = false;

    function update() {
      var y = window.pageYOffset || document.documentElement.scrollTop || 0;
      var shrunk = nav.classList.contains('is-shrunk');
      if (!shrunk && y > SHRINK_AT) nav.classList.add('is-shrunk');
      else if (shrunk && y < GROW_AT) nav.classList.remove('is-shrunk');
      ticking = false;
    }

    function onScroll() {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(update);
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    update();
  }

  // --- 3c. TIME-3 chronological-tick ---------------------------------------
  // Phase X.7d Causa retrofit slice 02 · TIME-3 chronological-tick-horizontal
  // pattern. Profile-gated via `body[data-motion-time3="1"]`; only Causa's
  // `g2-editorial-counter` profile opts in today. The CSS rule pair
  // `body.lm-ready:not(.lm-reduced)[data-motion-time3="1"] .chronotick`
  // hides the rail (scaleX 0) + ticks (opacity 0) by default; this
  // observer adds `.is-drawn` on viewport entry to play back the rail
  // draw + 80ms-staggered tick reveal. Once unobserved, no re-trigger
  // — same one-shot semantics as setupCounters/setupReveals. Reduced-
  // motion is already short-circuited at init() above; the CSS default-
  // visible baseline carries the static milestone strip for those
  // clients without further JS.
  function setupTime3() {
    if (document.body.getAttribute('data-motion-time3') !== '1') return;
    var strips = document.querySelectorAll('[data-time3]');
    if (!strips.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-drawn');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.25, rootMargin: '0px 0px -60px 0px' });

    strips.forEach(function (el) { io.observe(el); });
  }

  // --- 4. Marquee duplication ----------------------------------------------
  // The CSS keyframe translates -50% to create a seamless loop, which only
  // works if the track contains exactly two copies of the content. We do the
  // duplication here so template authors only write the content once.
  function setupMarquees() {
    var tracks = document.querySelectorAll('[data-lm="marquee"] .lm-marquee-track');
    tracks.forEach(function (track) {
      if (track.getAttribute('data-lm-duplicated') === '1') return;
      var clone = track.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      // Append each child of the clone into the original track so the flex row
      // contains two sequential copies — keeps the CSS rule self-contained.
      while (clone.firstChild) {
        track.appendChild(clone.firstChild);
      }
      track.setAttribute('data-lm-duplicated', '1');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
