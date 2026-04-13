/* ============================================================================
 * MarketWeb — Live Interactions (premium interactive components)
 * ============================================================================
 *
 * Zero-dependency interactive runtime for live_templates skins.
 * Pairs with static/css/live-interactions.css.
 *
 * Components
 *   1. Accordion — [data-li="accordion"]
 *   2. Lightbox — [data-li="lightbox-trigger"]
 *   3. Sticky CTA bar — [data-li="sticky-cta"]
 *
 * Safe to load `defer`. Runs on DOMContentLoaded.
 * Respects prefers-reduced-motion for all transitions.
 * ============================================================================ */

(function () {
  'use strict';

  function init() {
    setupAccordions();
    setupLightbox();
    setupStickyCTA();
    setupTabs();
    setupCompare();
    setupAnchorNav();
  }

  // --- 1. ACCORDIONS ---------------------------------------------------------
  // Parent: [data-li="accordion"]. Children: .li-acc-item > .li-acc-head + .li-acc-body
  // By default the first item can be open via .is-open class in HTML.
  // Clicking a head toggles its item; optionally closes siblings if
  // data-li-single="true" on the parent.

  function setupAccordions() {
    var accordions = document.querySelectorAll('[data-li="accordion"]');
    if (!accordions.length) return;

    accordions.forEach(function (acc) {
      var single = acc.getAttribute('data-li-single') === 'true';
      var heads = acc.querySelectorAll('.li-acc-head');

      // Measure and set initial max-height on open items
      acc.querySelectorAll('.li-acc-item.is-open .li-acc-body').forEach(function (body) {
        body.style.maxHeight = body.scrollHeight + 'px';
      });

      heads.forEach(function (head) {
        head.addEventListener('click', function () {
          var item = head.closest('.li-acc-item');
          if (!item) return;

          var isOpen = item.classList.contains('is-open');
          var body = item.querySelector('.li-acc-body');

          // Close siblings if single-open mode
          if (single && !isOpen) {
            acc.querySelectorAll('.li-acc-item.is-open').forEach(function (sib) {
              sib.classList.remove('is-open');
              var sibBody = sib.querySelector('.li-acc-body');
              if (sibBody) sibBody.style.maxHeight = '0px';
            });
          }

          // Toggle current
          if (isOpen) {
            item.classList.remove('is-open');
            if (body) body.style.maxHeight = '0px';
          } else {
            item.classList.add('is-open');
            if (body) body.style.maxHeight = body.scrollHeight + 'px';
          }
        });

        // Keyboard: Enter/Space toggle
        head.setAttribute('role', 'button');
        head.setAttribute('tabindex', '0');
        head.addEventListener('keydown', function (e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            head.click();
          }
        });
      });
    });
  }

  // --- 2. LIGHTBOX -----------------------------------------------------------
  // Any element with data-li="lightbox-trigger" opens a modal with the image.
  // data-li-src: image URL. data-li-caption: optional caption.
  // data-li-group: optional group name for prev/next navigation.

  var lightboxEl = null;
  var lightboxImg = null;
  var lightboxCaption = null;
  var lightboxGroup = [];
  var lightboxIndex = 0;

  function setupLightbox() {
    var triggers = document.querySelectorAll('[data-li="lightbox-trigger"]');
    if (!triggers.length) return;

    // Create lightbox DOM once
    lightboxEl = document.createElement('div');
    lightboxEl.className = 'li-lightbox';
    lightboxEl.innerHTML =
      '<div class="li-lb-close" aria-label="Close"></div>' +
      '<div class="li-lb-nav li-lb-prev" aria-label="Previous">\u2039</div>' +
      '<img src="" alt="">' +
      '<div class="li-lb-nav li-lb-next" aria-label="Next">\u203A</div>' +
      '<div class="li-lb-caption"></div>';
    document.body.appendChild(lightboxEl);

    lightboxImg = lightboxEl.querySelector('img');
    lightboxCaption = lightboxEl.querySelector('.li-lb-caption');
    var closeBtn = lightboxEl.querySelector('.li-lb-close');
    var prevBtn = lightboxEl.querySelector('.li-lb-prev');
    var nextBtn = lightboxEl.querySelector('.li-lb-next');

    // Event: close
    closeBtn.addEventListener('click', closeLightbox);
    lightboxEl.addEventListener('click', function (e) {
      if (e.target === lightboxEl) closeLightbox();
    });

    // Event: keyboard
    document.addEventListener('keydown', function (e) {
      if (!lightboxEl.classList.contains('is-active')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') navigateLightbox(-1);
      if (e.key === 'ArrowRight') navigateLightbox(1);
    });

    // Event: nav
    prevBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      navigateLightbox(-1);
    });
    nextBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      navigateLightbox(1);
    });

    // Bind triggers
    triggers.forEach(function (trigger) {
      trigger.style.cursor = 'zoom-in';
      trigger.addEventListener('click', function (e) {
        e.preventDefault();
        openLightbox(trigger);
      });
    });
  }

  function openLightbox(trigger) {
    var src = trigger.getAttribute('data-li-src') || trigger.querySelector('img')?.src || '';
    var caption = trigger.getAttribute('data-li-caption') || '';
    var group = trigger.getAttribute('data-li-group') || '';

    // Build group array
    if (group) {
      lightboxGroup = Array.from(
        document.querySelectorAll('[data-li="lightbox-trigger"][data-li-group="' + group + '"]')
      );
      lightboxIndex = lightboxGroup.indexOf(trigger);
    } else {
      lightboxGroup = [trigger];
      lightboxIndex = 0;
    }

    showLightboxImage(src, caption);
    lightboxEl.classList.add('is-active');
    document.body.style.overflow = 'hidden';

    // Show/hide nav arrows
    var nav = lightboxEl.querySelectorAll('.li-lb-nav');
    var showNav = lightboxGroup.length > 1;
    nav.forEach(function (n) { n.style.display = showNav ? '' : 'none'; });
  }

  function closeLightbox() {
    if (!lightboxEl) return;
    lightboxEl.classList.remove('is-active');
    document.body.style.overflow = '';
  }

  function navigateLightbox(dir) {
    if (lightboxGroup.length < 2) return;
    lightboxIndex = (lightboxIndex + dir + lightboxGroup.length) % lightboxGroup.length;
    var trigger = lightboxGroup[lightboxIndex];
    var src = trigger.getAttribute('data-li-src') || trigger.querySelector('img')?.src || '';
    var caption = trigger.getAttribute('data-li-caption') || '';
    showLightboxImage(src, caption);
  }

  function showLightboxImage(src, caption) {
    if (!lightboxImg) return;
    lightboxImg.src = src;
    lightboxImg.alt = caption || '';
    lightboxCaption.textContent = caption || '';
    lightboxCaption.style.display = caption ? '' : 'none';
  }

  // --- 3. STICKY CTA BAR ----------------------------------------------------
  // [data-li="sticky-cta"] with data-li-trigger="selector" (element to scroll past)
  // Shows bar after user scrolls past the trigger element.

  function setupStickyCTA() {
    var bar = document.querySelector('[data-li="sticky-cta"]');
    if (!bar) return;

    var triggerSelector = bar.getAttribute('data-li-trigger') || '.sp-hero, .sp-hero-em, .fd-hero';
    var triggerEl = document.querySelector(triggerSelector);
    if (!triggerEl) return;

    // Use IntersectionObserver to detect when hero exits viewport
    if (!('IntersectionObserver' in window)) {
      // No IO: just show the bar after a delay
      setTimeout(function () { bar.classList.add('is-visible'); }, 2000);
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          bar.classList.remove('is-visible');
        } else {
          // Only show when scrolled DOWN past hero (not when at top)
          if (entry.boundingClientRect.top < 0) {
            bar.classList.add('is-visible');
          }
        }
      });
    }, { threshold: 0 });

    io.observe(triggerEl);
  }

  // --- 4. TABS --------------------------------------------------------------
  // [data-li="tabs"] with .li-tabs-nav containing .li-tab-btn[data-li-target="id"]
  // and matching .li-tab-panel[data-li-id="id"] elements.
  // The currently active button carries .is-active; the matching panel mirrors it.

  function setupTabs() {
    var groups = document.querySelectorAll('[data-li="tabs"]');
    if (!groups.length) return;

    groups.forEach(function (group) {
      var buttons = group.querySelectorAll('.li-tab-btn');
      var panels = group.querySelectorAll('.li-tab-panel');
      if (!buttons.length || !panels.length) return;

      // Ensure at least one tab is active
      var hasActive = Array.from(buttons).some(function (b) {
        return b.classList.contains('is-active');
      });
      if (!hasActive) {
        buttons[0].classList.add('is-active');
        var firstTarget = buttons[0].getAttribute('data-li-target');
        var firstPanel = group.querySelector('.li-tab-panel[data-li-id="' + firstTarget + '"]');
        if (firstPanel) firstPanel.classList.add('is-active');
      } else {
        // Mirror the active button onto its panel
        Array.from(buttons).forEach(function (b) {
          if (b.classList.contains('is-active')) {
            var target = b.getAttribute('data-li-target');
            var panel = group.querySelector('.li-tab-panel[data-li-id="' + target + '"]');
            if (panel) panel.classList.add('is-active');
          }
        });
      }

      buttons.forEach(function (btn) {
        btn.setAttribute('role', 'tab');
        btn.setAttribute('tabindex', '0');

        btn.addEventListener('click', function () {
          activateTab(group, btn);
        });
        btn.addEventListener('keydown', function (e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            activateTab(group, btn);
          }
          // Optional arrow-key navigation
          if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
            e.preventDefault();
            var list = Array.from(buttons);
            var idx = list.indexOf(btn);
            var next = e.key === 'ArrowRight'
              ? list[(idx + 1) % list.length]
              : list[(idx - 1 + list.length) % list.length];
            if (next) {
              next.focus();
              activateTab(group, next);
            }
          }
        });
      });
    });
  }

  function activateTab(group, btn) {
    var target = btn.getAttribute('data-li-target');
    group.querySelectorAll('.li-tab-btn').forEach(function (b) {
      b.classList.toggle('is-active', b === btn);
    });
    group.querySelectorAll('.li-tab-panel').forEach(function (p) {
      p.classList.toggle('is-active', p.getAttribute('data-li-id') === target);
    });
  }

  // --- 5. COMPARE (Before / After) -----------------------------------------
  // [data-li="compare"] containing .li-cmp-before and .li-cmp-after absolute layers.
  // Drag or click-to-move, keyboard support via left/right arrows on container focus.

  function setupCompare() {
    var panels = document.querySelectorAll('[data-li="compare"]');
    if (!panels.length) return;

    panels.forEach(function (panel) {
      // Ensure a handle exists
      var handle = panel.querySelector('.li-cmp-handle');
      if (!handle) {
        handle = document.createElement('div');
        handle.className = 'li-cmp-handle';
        panel.appendChild(handle);
      }

      var after = panel.querySelector('.li-cmp-after');
      if (!after) return;

      function setPosition(pct) {
        var clamped = Math.max(2, Math.min(98, pct));
        after.style.clipPath = 'inset(0 0 0 ' + clamped + '%)';
        handle.style.left = clamped + '%';
      }

      function onMove(clientX) {
        var rect = panel.getBoundingClientRect();
        var pct = ((clientX - rect.left) / rect.width) * 100;
        setPosition(pct);
      }

      // Mouse
      panel.addEventListener('mousedown', function (e) {
        panel.classList.add('is-dragging');
        onMove(e.clientX);
        function onMouseMove(ev) { onMove(ev.clientX); }
        function onMouseUp() {
          panel.classList.remove('is-dragging');
          document.removeEventListener('mousemove', onMouseMove);
          document.removeEventListener('mouseup', onMouseUp);
        }
        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
      });

      // Touch
      panel.addEventListener('touchstart', function (e) {
        if (!e.touches.length) return;
        panel.classList.add('is-dragging');
        onMove(e.touches[0].clientX);
      }, { passive: true });
      panel.addEventListener('touchmove', function (e) {
        if (!e.touches.length) return;
        onMove(e.touches[0].clientX);
      }, { passive: true });
      panel.addEventListener('touchend', function () {
        panel.classList.remove('is-dragging');
      });

      // Keyboard (focus container via tabindex="0" in HTML)
      panel.addEventListener('keydown', function (e) {
        var currentLeft = parseFloat(handle.style.left) || 50;
        if (e.key === 'ArrowLeft') { e.preventDefault(); setPosition(currentLeft - 4); }
        if (e.key === 'ArrowRight') { e.preventDefault(); setPosition(currentLeft + 4); }
      });

      // Initial position
      setPosition(50);
    });
  }

  // --- 6. ANCHOR SUBNAV -----------------------------------------------------
  // .li-anchor-nav with anchor links [href="#id"]. Tags the currently-visible
  // section via IntersectionObserver. Enhances the sticky nav with `.is-active`
  // on the link whose target is in viewport.

  function setupAnchorNav() {
    var nav = document.querySelector('.li-anchor-nav');
    if (!nav) return;
    var links = nav.querySelectorAll('a[href^="#"]');
    if (!links.length) return;

    var targets = [];
    links.forEach(function (a) {
      var id = a.getAttribute('href').slice(1);
      var el = document.getElementById(id);
      if (el) targets.push({ id: id, el: el, link: a });
    });
    if (!targets.length) return;

    if (!('IntersectionObserver' in window)) return;

    var byId = {};
    targets.forEach(function (t) { byId[t.id] = t.link; });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = byId[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting && entry.intersectionRatio > 0.25) {
          links.forEach(function (l) { l.classList.remove('is-active'); });
          link.classList.add('is-active');
        }
      });
    }, { threshold: [0, 0.25, 0.5], rootMargin: '-100px 0px -50% 0px' });

    targets.forEach(function (t) { io.observe(t.el); });

    // Smooth scroll when clicking an anchor
    links.forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href').slice(1);
        var el = document.getElementById(id);
        if (!el) return;
        e.preventDefault();
        var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        el.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
      });
    });
  }

  // --- INIT ------------------------------------------------------------------
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
