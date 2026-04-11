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

    setupReveals();
    setupStaggers();
    setupCounters();
    setupMarquees();
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
    // Parse leading numeric portion + preserve suffix (e.g. "180€" or "1.4k")
    var match = original.match(/^(-?\d+(?:[.,]\d+)?)(.*)$/);
    if (!match) return;

    var target = parseFloat((el.getAttribute('data-lm-to') || match[1]).replace(',', '.'));
    var suffix = match[2] || '';
    var isInt = String(target).indexOf('.') === -1;
    var decimals = isInt ? 0 : (String(target).split('.')[1] || '').length;

    if (isNaN(target)) return;

    // Cache the pristine text so we never double-animate on re-observation.
    el.setAttribute('data-lm-original', original);

    var start = performance.now();
    function ease(t) { return 1 - Math.pow(1 - t, 3); } // easeOutCubic

    function frame(now) {
      var t = Math.min(1, (now - start) / COUNTER_DURATION_MS);
      var value = target * ease(t);
      el.innerText = (isInt ? Math.round(value) : value.toFixed(decimals)) + suffix;
      if (t < 1) requestAnimationFrame(frame);
      else el.innerText = (isInt ? Math.round(target) : target.toFixed(decimals)) + suffix;
    }
    requestAnimationFrame(frame);
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
