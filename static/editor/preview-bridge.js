/* Preview Bridge — Phase A.2
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

  function paintHighlight(selector, labelText) {
    clearHighlight();
    if (!selector) return;

    let els;
    try { els = document.querySelectorAll(selector); }
    catch (e) { return; }

    if (!els || !els.length) return;

    const layer = getOverlayLayer();
    let minTop = Infinity, minLeft = Infinity;

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

      // Soft scroll into view if the ring is off-screen
      if (rect.top < 60 || rect.bottom > window.innerHeight - 40) {
        el.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    });

    if (labelText && minTop !== Infinity) {
      const label = getLabel();
      label.textContent = labelText;
      label.style.top  = Math.max(8, minTop - 28) + "px";
      label.style.left = Math.max(8, minLeft) + "px";
      requestAnimationFrame(() => label.classList.add("is-visible"));
    }
  }

  let lastSelector = "";
  let lastLabel = "";

  window.addEventListener("message", (event) => {
    if (event.origin !== ALLOWED_ORIGIN) return;
    const data = event.data || {};
    if (data.source !== "mw-editor") return;
    if (data.kind === "highlight") {
      lastSelector = data.selector || "";
      lastLabel = data.label || "";
      paintHighlight(lastSelector, lastLabel);
    }
  });

  // Re-paint on resize / scroll so the ring tracks the target
  function reposition() { if (lastSelector) paintHighlight(lastSelector, lastLabel); }
  window.addEventListener("resize", reposition);
  window.addEventListener("scroll", reposition, { passive: true });

  // A.2.1: DO NOT clear on idle inside the iframe. The editor owns
  // the clear decision (it knows whether a sidebar field still has
  // focus). A stale ring is much better than a missing ring while
  // the user types into a field.
})();
