/* Preview Bridge — Phase A.2 / A.2.4
 *
 * Runs inside the LiveTemplateView iframe only when a project preview
 * is active (injected by the per-archetype _base template behind an
 * {% if preview_project %} guard).
 *
 * Listens for window.postMessage from the editor and paints an
 * elegant overlay highlight on the element(s) matching the supplied
 * CSS selector. The effect is deliberately subtle — a soft amber
 * glow + dashed outline — so it reinforces the mapping between the
 * sidebar field and the live region without hijacking the preview.
 *
 * A.2.4 — deterministic field targeting:
 *   paintRings() ONLY positions the ring overlays — never scrolls.
 *   maybeScrollToTarget() is the single scroll gate: it runs at most
 *   once per explicit activation (message with `scroll: true`), only
 *   if the target is off-screen, and dedups same-target re-activations
 *   so repaints from autosave reload, resize, or manual iframe scroll
 *   never auto-follow the user.
 */
(function () {
  "use strict";

  const STYLE_ID = "mw-edit-highlight-style";
  const OVERLAY_ID = "mw-edit-highlight-overlays";
  const LABEL_ID = "mw-edit-highlight-label";
  const ALLOWED_ORIGIN = window.location.origin;

  // Insert styles once
  if (!document.getElementById(STYLE_ID)) {
    const s = document.createElement("style");
    s.id = STYLE_ID;
    s.textContent = `
      #${OVERLAY_ID} {
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 2147483000;
      }
      #${OVERLAY_ID} .mw-edit-ring {
        position: absolute;
        border-radius: 10px;
        box-shadow:
          0 0 0 2px rgba(245, 158, 11, 0.92),
          0 0 0 6px rgba(245, 158, 11, 0.22),
          0 18px 48px rgba(245, 158, 11, 0.28);
        transition: top 220ms cubic-bezier(0.2, 0.8, 0.2, 1),
                    left 220ms cubic-bezier(0.2, 0.8, 0.2, 1),
                    width 220ms cubic-bezier(0.2, 0.8, 0.2, 1),
                    height 220ms cubic-bezier(0.2, 0.8, 0.2, 1);
        pointer-events: none;
        opacity: 0;
        animation: mwEditFade 220ms forwards, mwEditPulse 2600ms 260ms infinite ease-in-out;
      }
      #${OVERLAY_ID} .mw-edit-ring::before {
        content: "";
        position: absolute;
        inset: -3px;
        border-radius: 12px;
        border: 1px dashed rgba(245, 158, 11, 0.55);
      }
      @keyframes mwEditFade {
        from { opacity: 0; transform: scale(0.985); }
        to   { opacity: 1; transform: scale(1); }
      }
      @keyframes mwEditPulse {
        0%, 100% {
          box-shadow:
            0 0 0 2px rgba(245, 158, 11, 0.92),
            0 0 0 6px rgba(245, 158, 11, 0.22),
            0 18px 48px rgba(245, 158, 11, 0.28);
        }
        50% {
          box-shadow:
            0 0 0 2px rgba(245, 158, 11, 1),
            0 0 0 10px rgba(245, 158, 11, 0.12),
            0 22px 60px rgba(245, 158, 11, 0.35);
        }
      }
      @media (prefers-reduced-motion: reduce) {
        #${OVERLAY_ID} .mw-edit-ring { animation: mwEditFade 220ms forwards; }
      }
      #${LABEL_ID} {
        position: fixed;
        padding: 5px 11px 5px 9px;
        border-radius: 999px;
        background: rgba(11, 13, 16, 0.92);
        color: #fff;
        font: 500 11px/1 'Inter', system-ui, sans-serif;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        z-index: 2147483001;
        pointer-events: none;
        opacity: 0;
        transform: translateY(-4px);
        transition: opacity 180ms, transform 180ms;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        white-space: nowrap;
      }
      #${LABEL_ID}::before {
        content: "";
        display: inline-block;
        width: 6px; height: 6px; border-radius: 50%;
        background: #f59e0b;
      }
      #${LABEL_ID}.is-visible { opacity: 1; transform: translateY(0); }
    `;
    document.head.appendChild(s);
  }

  function getOverlayLayer() {
    let el = document.getElementById(OVERLAY_ID);
    if (!el) {
      el = document.createElement("div");
      el.id = OVERLAY_ID;
      document.body.appendChild(el);
    }
    return el;
  }

  function getLabel() {
    let el = document.getElementById(LABEL_ID);
    if (!el) {
      el = document.createElement("div");
      el.id = LABEL_ID;
      document.body.appendChild(el);
    }
    return el;
  }

  function clearHighlight() {
    const layer = document.getElementById(OVERLAY_ID);
    if (layer) layer.innerHTML = "";
    const label = document.getElementById(LABEL_ID);
    if (label) label.classList.remove("is-visible");
  }

  // Paint-only — positions the rings + label, NEVER scrolls.
  // Safe to call on every resize / scroll event.
  function paintRings(selector, labelText) {
    clearHighlight();
    if (!selector) return null;

    let els;
    try { els = document.querySelectorAll(selector); }
    catch (e) { return null; }

    if (!els || !els.length) return null;

    const layer = getOverlayLayer();
    let minTop = Infinity, minLeft = Infinity;
    let firstVisible = null;

    els.forEach((el) => {
      const rect = el.getBoundingClientRect();
      if (rect.width <= 0 || rect.height <= 0) return;
      const ring = document.createElement("div");
      ring.className = "mw-edit-ring";
      // Pad the ring 4px outward for optical balance
      ring.style.top    = (rect.top - 4) + "px";
      ring.style.left   = (rect.left - 4) + "px";
      ring.style.width  = (rect.width + 8) + "px";
      ring.style.height = (rect.height + 8) + "px";
      layer.appendChild(ring);

      if (rect.top < minTop) { minTop = rect.top; minLeft = rect.left; }
      if (!firstVisible) firstVisible = el;
    });

    if (labelText && minTop !== Infinity) {
      const label = getLabel();
      label.textContent = labelText;
      label.style.top  = Math.max(8, minTop - 28) + "px";
      label.style.left = Math.max(8, minLeft) + "px";
      requestAnimationFrame(() => label.classList.add("is-visible"));
    }
    return firstVisible;
  }

  // Scroll gate — runs at most once per explicit activation.
  // Dedups same-target re-activations; only scrolls if the target is
  // meaningfully off-screen; never centres an element that is already
  // visible ("nearest" keeps the camera calm).
  let lastScrolledSelector = "";
  function maybeScrollToTarget(el, selector) {
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const vh = window.innerHeight || document.documentElement.clientHeight;
    const fullyVisible = rect.top >= 8 && rect.bottom <= vh - 8;
    const largelyVisible = rect.top >= -rect.height * 0.2
                        && rect.bottom <= vh + rect.height * 0.2;
    if (fullyVisible) { lastScrolledSelector = selector; return; }
    // If we just scrolled to this exact selector AND it is still
    // largely in view, do not scroll again (guards against autosave
    // reload re-activation and rapid re-focus).
    if (selector && selector === lastScrolledSelector && largelyVisible) return;
    lastScrolledSelector = selector;
    try {
      el.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "nearest" });
    } catch (e) {
      el.scrollIntoView(true);
    }
  }

  let lastSelector = "";
  let lastLabel = "";

  window.addEventListener("message", (event) => {
    if (event.origin !== ALLOWED_ORIGIN) return;
    const data = event.data || {};
    if (data.source !== "mw-editor") return;
    if (data.kind === "highlight") {
      const selector = data.selector || "";
      const label = data.label || "";
      const shouldScroll = data.scroll === true;
      // Clearing highlight: reset dedup so the next activation can
      // scroll if needed.
      if (!selector) { lastScrolledSelector = ""; }
      lastSelector = selector;
      lastLabel = label;
      const firstVisible = paintRings(selector, label);
      if (shouldScroll && firstVisible) {
        maybeScrollToTarget(firstVisible, selector);
      }
    }
  });

  // Keep rings glued to their target during manual user scroll /
  // resize. This NEVER scrolls — it only re-measures and repositions
  // the existing ring rectangles. Breaks the old feedback loop where
  // scroll → paint → scrollIntoView → scroll.
  let repositionTicking = false;
  function reposition() {
    if (!lastSelector) return;
    if (repositionTicking) return;
    repositionTicking = true;
    requestAnimationFrame(() => {
      paintRings(lastSelector, lastLabel);
      repositionTicking = false;
    });
  }
  window.addEventListener("resize", reposition);
  window.addEventListener("scroll", reposition, { passive: true });

  // A.2.1: DO NOT clear on idle inside the iframe. The editor owns
  // the clear decision (it knows whether a sidebar field still has
  // focus). A stale ring is much better than a missing ring while
  // the user types into a field.
})();
