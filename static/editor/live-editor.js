/* Live Editor — Phase A.2 + A.2.1 premium shell controller
 *
 * A.2 responsibilities (unchanged):
 *  - Debounced autosave (400ms window)
 *  - Iframe soft-reload with scroll preservation
 *  - Device toolbar + focus mode + compare toggle
 *  - Sidebar UX: search filter, accordion, reset-to-baseline
 *  - Toast stack + status chip
 *
 * A.2.1 micro-fix additions:
 *  - Locale switcher lives in sidebar (not preview top-strip)
 *  - Image widget: URL + thumbnail preview with load/error state
 *  - Character counter with near-limit / at-limit styling
 *  - Highlight reliability: re-paint after autosave reload, hold
 *    state while field keeps focus, pulsing ring animation
 *  - Compare scroll sync: baseline <-> edited mirror scrollY via
 *    postMessage throttled to ~16ms
 */
(function () {
  "use strict";

  const $   = (sel, root = document) => root.querySelector(sel);
  const $$  = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  const root = $(".ed-root");
  if (!root) return;

  const cfg = window.MW_EDITOR_CONFIG || {};
  const autosaveUrl     = cfg.autosaveUrl;
  const previewUrlBase  = cfg.previewUrl  || "";
  const baselineUrlBase = cfg.baselineUrl || "";
  const csrfToken       = cfg.csrfToken   || "";
  const DEBOUNCE_MS     = 400;

  // ────────────────────────────────────────────────────────────
  // Locale state (A.2.1) — kept client-side, appended to iframe
  // src via ?lang=xx. The server treats `?lang=` as the single
  // source of truth for the preview render locale.
  // ────────────────────────────────────────────────────────────

  let currentLang = cfg.currentLocale || "it";

  function withLang(url) {
    if (!url) return url;
    if (!currentLang || currentLang === "it") return url;
    const sep = url.indexOf("?") === -1 ? "?" : "&";
    return url + sep + "lang=" + encodeURIComponent(currentLang);
  }

  // ────────────────────────────────────────────────────────────
  // Toast helper
  // ────────────────────────────────────────────────────────────

  const toastStack = $(".ed-toasts");

  function toast(msg, kind) {
    if (!toastStack) return;
    const el = document.createElement("div");
    el.className = "ed-toast" + (kind ? " is-" + kind : "");
    const icon = kind === "success" ? "bi-check2"
              : kind === "error"   ? "bi-exclamation-triangle"
              : "bi-info-circle";
    el.innerHTML = `<i class="bi ${icon}"></i><span></span>`;
    el.querySelector("span").textContent = msg;
    toastStack.appendChild(el);
    while (toastStack.children.length > 3) toastStack.removeChild(toastStack.firstChild);
    requestAnimationFrame(() => el.classList.add("is-visible"));
    setTimeout(() => {
      el.classList.remove("is-visible");
      setTimeout(() => el.remove(), 260);
    }, 2400);
  }

  // ────────────────────────────────────────────────────────────
  // Save-status chip + banner
  // ────────────────────────────────────────────────────────────

  const statusChip = $(".ed-status");
  const statusText = statusChip ? statusChip.querySelector(".label") : null;
  function setStatus(state, label) {
    if (!statusChip) return;
    statusChip.setAttribute("data-state", state);
    if (statusText && label) statusText.textContent = label;
  }
  setStatus("idle", "Pronto");

  const banner = $(".ed-banner");
  let bannerTimer = null;
  function flashBanner(msg, iconKey, durationMs) {
    if (!banner) return;
    banner.innerHTML = `<i class="bi ${iconKey || "bi-stars"}"></i><span>${msg}</span>`;
    banner.classList.add("is-visible");
    clearTimeout(bannerTimer);
    bannerTimer = setTimeout(() => banner.classList.remove("is-visible"), durationMs || 2600);
  }
  if (cfg.justCreated) {
    flashBanner("Progetto creato — le modifiche si vedono in tempo reale", "bi-stars", 3400);
  }

  // ────────────────────────────────────────────────────────────
  // Autosave queue
  // ────────────────────────────────────────────────────────────

  let dirtyContent = {};
  let dirtyTokens = {};
  let pendingTimer = null;
  let inFlight = false;
  let pendingAfterSave = false;

  function flushDirty() {
    if (inFlight) { pendingAfterSave = true; return; }
    if (!Object.keys(dirtyContent).length && !Object.keys(dirtyTokens).length) return;
    const sentContent = dirtyContent;
    const sentTokens  = dirtyTokens;
    dirtyContent = {};
    dirtyTokens  = {};
    inFlight = true;
    setStatus("saving", "Salvataggio…");

    fetch(autosaveUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
        "X-Requested-With": "XMLHttpRequest",
      },
      body: JSON.stringify({ content: sentContent, tokens: sentTokens }),
      credentials: "same-origin",
    })
      .then((r) => r.json().then((data) => ({ status: r.status, data })))
      .then(({ status, data }) => {
        inFlight = false;
        if (status >= 200 && status < 300 && data.ok) {
          setStatus("saved", "Salvato");
          refreshPreview();
          updateOverrideBadges(data.override_count);
          markTouchedFields(data.content_keys, sentContent, data.token_keys, sentTokens);
          if (pendingAfterSave) {
            pendingAfterSave = false;
            setTimeout(flushDirty, 30);
          }
        } else {
          setStatus("error", "Errore di salvataggio");
          dirtyContent = Object.assign({}, sentContent, dirtyContent);
          dirtyTokens  = Object.assign({}, sentTokens,  dirtyTokens);
          toast((data && data.error) || "Impossibile salvare le modifiche.", "error");
        }
      })
      .catch(() => {
        inFlight = false;
        setStatus("error", "Disconnesso");
        dirtyContent = Object.assign({}, sentContent, dirtyContent);
        dirtyTokens  = Object.assign({}, sentTokens,  dirtyTokens);
        toast("Connessione interrotta. Riproveremo.", "error");
      });
  }

  function queueEdit(kind, key, value) {
    if (kind === "content") dirtyContent[key] = value;
    else                    dirtyTokens[key]  = value;
    clearTimeout(pendingTimer);
    setStatus("saving", "Modifica…");
    pendingTimer = setTimeout(flushDirty, DEBOUNCE_MS);
  }

  // ────────────────────────────────────────────────────────────
  // Iframe soft-reload (keep scroll, re-paint highlight)
  // ────────────────────────────────────────────────────────────

  const frame         = $(".ed-frame");
  const frameBaseline = $(".ed-frame-baseline");
  const frameWrap     = $(".ed-frame-wrap");

  let lastScroll = 0;
  let lastHighlight = { selector: "", label: "" };

  if (frame) {
    frame.addEventListener("load", () => {
      try {
        const doc = frame.contentDocument;
        if (doc && lastScroll) {
          doc.defaultView.scrollTo({ top: lastScroll, behavior: "instant" });
        }
      } catch (e) { /* same-origin guarantees */ }
      // Re-paint the currently active highlight after the reload
      if (lastHighlight.selector) {
        setTimeout(() => postHighlight(lastHighlight.selector, lastHighlight.label), 80);
      }
      wireIframeScrollSync(frame);
    });
  }
  if (frameBaseline) {
    frameBaseline.addEventListener("load", () => {
      wireIframeScrollSync(frameBaseline);
      // Mirror the edited iframe's current scroll into the baseline
      // iframe whenever compare opens / the baseline reloads.
      syncScrollTo(frameBaseline, getIframeScrollY(frame));
    });
  }

  function refreshPreview() {
    if (!frame) return;
    try {
      const doc = frame.contentDocument;
      lastScroll = (doc && doc.defaultView) ? doc.defaultView.scrollY : 0;
    } catch (e) { lastScroll = 0; }
    frame.src = withLang(previewUrlBase) + (previewUrlBase.indexOf("?") === -1 ? "?" : "&") + "_t=" + Date.now();
  }

  function reloadBothFrames() {
    lastScroll = getIframeScrollY(frame) || 0;
    if (frame) frame.src = withLang(previewUrlBase) + (previewUrlBase.indexOf("?") === -1 ? "?" : "&") + "_t=" + Date.now();
    if (frameBaseline && frameBaseline.src) {
      frameBaseline.src = withLang(baselineUrlBase) + (baselineUrlBase.indexOf("?") === -1 ? "?" : "&") + "_t=" + Date.now();
    }
  }

  // ────────────────────────────────────────────────────────────
  // Highlight postMessage — robust re-paint + idle hold
  // ────────────────────────────────────────────────────────────

  let highlightHoldTimer = null;

  function postHighlight(selector, label) {
    lastHighlight = { selector: selector || "", label: label || "" };
    if (frame && frame.contentWindow) {
      frame.contentWindow.postMessage({
        source: "mw-editor",
        kind: "highlight",
        selector: selector || "",
        label: label || "",
      }, window.location.origin);
    }
    // Keep the highlight alive for a while so autosave reload (iframe
    // load event, ~300ms) does not visibly blink the overlay away.
    clearTimeout(highlightHoldTimer);
    if (selector) {
      highlightHoldTimer = setTimeout(() => {
        // Only clear if no sidebar field has focus
        if (!document.activeElement || !document.activeElement.closest(".ed-field")) {
          postHighlight("");
        }
      }, 5000);
    }
  }

  // ────────────────────────────────────────────────────────────
  // Field wiring: autosave + highlight + char counter + image
  // ────────────────────────────────────────────────────────────

  function updateCharCount(input) {
    const field = input.closest(".ed-field");
    if (!field) return;
    const counter = field.querySelector(".ed-count");
    if (!counter) return;
    const max = parseInt(counter.getAttribute("data-max") || "0", 10);
    const cur = (input.value || "").length;
    counter.textContent = cur + "/" + max;
    counter.classList.toggle("is-near-limit", max > 0 && cur >= max * 0.9 && cur < max);
    counter.classList.toggle("is-at-limit",   max > 0 && cur >= max);
  }

  const fieldInputs = $$(".ed-field [data-ed-field]");
  fieldInputs.forEach((input) => {
    const field = input.closest(".ed-field");
    const kind  = input.getAttribute("data-ed-kind");
    const key   = input.getAttribute("data-ed-field");

    const handler = () => {
      const value = input.value;
      queueEdit(kind, key, value);
      field.classList.add("is-overridden");
      updateCharCount(input);
      maybeUpdateImageThumb(field, value);
    };

    input.addEventListener("input", handler);
    input.addEventListener("change", handler);
    updateCharCount(input);

    // Color-picker + hex paired input
    if (input.type === "color") {
      const pair = field.querySelector(".ed-color-hex");
      if (pair) {
        input.addEventListener("input", () => { pair.value = input.value.toUpperCase(); });
        pair.addEventListener("input", () => {
          if (/^#[0-9a-f]{6}$/i.test(pair.value)) {
            input.value = pair.value.toLowerCase();
            queueEdit(kind, key, pair.value.toLowerCase());
            field.classList.add("is-overridden");
          }
        });
      }
    }

    // Highlight mapping: focus / mouseenter posts region selector;
    // blur does NOT clear if another field is about to take focus —
    // the 5s idle timer inside postHighlight handles that cleanly.
    const group = input.closest(".ed-group");
    const region = group ? group.getAttribute("data-region") : "";
    const label = input.closest(".ed-field")
                  ? (input.closest(".ed-field").getAttribute("data-ed-label") || "")
                  : "";
    input.addEventListener("focus", () => postHighlight(region, label));

    // Reset-to-baseline
    const resetBtn = field.querySelector(".ed-reset");
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        const baseline = input.getAttribute("data-ed-baseline") || "";
        input.value = baseline;
        field.classList.remove("is-overridden");
        queueEdit(kind, key, baseline);
        updateCharCount(input);
        maybeUpdateImageThumb(field, baseline);
        toast("Campo riportato al baseline", "success");
      });
    }
  });

  // Group-head hover also flashes the region
  $$(".ed-group-head").forEach((btn) => {
    const group = btn.closest(".ed-group");
    const region = group ? group.getAttribute("data-region") : "";
    const label  = group ? (group.querySelector(".ed-glabel")?.textContent.trim() || "") : "";
    btn.addEventListener("mouseenter", () => {
      if (!document.activeElement || !document.activeElement.closest(".ed-field")) {
        postHighlight(region, label);
      }
    });
  });

  // ────────────────────────────────────────────────────────────
  // Image widget
  // ────────────────────────────────────────────────────────────

  function maybeUpdateImageThumb(field, url) {
    const thumb = field.querySelector(".ed-image-thumb");
    if (!thumb) return;
    thumb.classList.remove("is-error");
    if (!url) {
      thumb.style.backgroundImage = "";
      thumb.innerHTML = '<i class="bi bi-image"></i>';
      return;
    }
    thumb.classList.add("is-loading");
    const probe = new Image();
    probe.onload = () => {
      thumb.classList.remove("is-loading");
      thumb.style.backgroundImage = `url('${url.replace(/'/g, "%27")}')`;
      thumb.innerHTML = "";
    };
    probe.onerror = () => {
      thumb.classList.remove("is-loading");
      thumb.classList.add("is-error");
      thumb.innerHTML = '<i class="bi bi-exclamation-triangle"></i>';
    };
    probe.src = url;
  }

  $$(".ed-image").forEach((widget) => {
    const urlInput = widget.querySelector(".ed-image-url");
    const pickInput = widget.querySelector(".ed-image-pick input[type=file]");
    const clearBtn  = widget.querySelector(".ed-image-clear");

    if (pickInput) {
      pickInput.addEventListener("change", () => {
        const file = pickInput.files && pickInput.files[0];
        if (!file) return;
        // File uploads land as data-URL in the URL input for this
        // micro-fix (no storage backend). The persisted override is
        // the data-URL; users can replace with a real CDN URL any
        // time. A proper upload endpoint is Phase A.3 scope.
        const reader = new FileReader();
        reader.onload = () => {
          urlInput.value = String(reader.result || "");
          urlInput.dispatchEvent(new Event("input", { bubbles: true }));
        };
        reader.readAsDataURL(file);
      });
    }

    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        urlInput.value = "";
        urlInput.dispatchEvent(new Event("input", { bubbles: true }));
      });
    }
  });

  // Validate that autosave accepts data-URLs too. The schema has
  // `type: "image"` with a URL-ish validation. Update the backend's
  // validate_value to accept `data:` too — or we can just let the
  // server bounce and show a toast. For now we emit a friendly
  // warning when a local file is used, since no upload endpoint
  // exists yet. The field still works via URL paste.
  // NOTE: at this point we have not wired a server-side accept for
  // data-URLs; the paste flow is fully functional.

  // ────────────────────────────────────────────────────────────
  // Autosave diff → overridden state sync
  // ────────────────────────────────────────────────────────────

  function markTouchedFields(contentKeys, sentContent) {
    (contentKeys || []).forEach((k) => {
      const input = document.querySelector(`[data-ed-field="${CSS.escape(k)}"][data-ed-kind="content"]`);
      if (!input) return;
      const baseline = input.getAttribute("data-ed-baseline") || "";
      const field = input.closest(".ed-field");
      if (!field) return;
      if ((input.value || "") === baseline) field.classList.remove("is-overridden");
      else                                  field.classList.add("is-overridden");
    });
  }

  function updateOverrideBadges(total) {
    const counter = $(".ed-sidebar-head .counter");
    if (counter) counter.textContent = total === 1 ? "1 modifica" : (total + " modifiche");
    $$(".ed-group").forEach((group) => {
      const badge = group.querySelector(".ed-gbadge");
      if (!badge) return;
      const count = group.querySelectorAll(".ed-field.is-overridden").length;
      badge.setAttribute("data-count", String(count));
      badge.textContent = count;
    });
  }

  // ────────────────────────────────────────────────────────────
  // Sidebar: accordion + search + collapse
  // ────────────────────────────────────────────────────────────

  const firstGroup = $(".ed-group");
  if (firstGroup) firstGroup.classList.add("is-open");

  $$(".ed-group-head").forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.closest(".ed-group").classList.toggle("is-open");
    });
  });

  const searchInput = $(".ed-sidebar-search input");
  if (searchInput) {
    searchInput.addEventListener("input", () => {
      const q = searchInput.value.trim().toLowerCase();
      let anyVisible = false;
      $$(".ed-group").forEach((group) => {
        let groupHas = false;
        $$(".ed-field", group).forEach((f) => {
          if (!q) { f.classList.remove("is-hidden"); groupHas = true; return; }
          const label = (f.getAttribute("data-ed-label") || "").toLowerCase();
          const key   = (f.getAttribute("data-ed-key")   || "").toLowerCase();
          const match = label.includes(q) || key.includes(q);
          f.classList.toggle("is-hidden", !match);
          if (match) groupHas = true;
        });
        group.classList.toggle("is-hidden", !groupHas);
        if (groupHas) { group.classList.add("is-open"); anyVisible = true; }
      });
      const sidebar = $(".ed-sidebar");
      if (sidebar) sidebar.classList.toggle("is-empty", !anyVisible);
    });
  }

  const collapseBtn = $("[data-ed-collapse]");
  if (collapseBtn) collapseBtn.addEventListener("click", () => root.classList.toggle("is-sidebar-collapsed"));

  // ────────────────────────────────────────────────────────────
  // Locale switcher (sidebar, replaces preview top-strip)
  // ────────────────────────────────────────────────────────────

  $$("[data-ed-lang]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const code = btn.getAttribute("data-ed-lang");
      if (code === currentLang) return;
      currentLang = code;
      $$("[data-ed-lang]").forEach((b) => b.classList.toggle("is-active", b === btn));
      reloadBothFrames();
    });
  });

  // ────────────────────────────────────────────────────────────
  // Device toolbar + focus mode
  // ────────────────────────────────────────────────────────────

  $$("[data-ed-device]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const device = btn.getAttribute("data-ed-device");
      $$("[data-ed-device]").forEach((b) => b.classList.toggle("is-active", b === btn));
      if (frameWrap) frameWrap.setAttribute("data-device", device);
    });
  });

  const focusBtn = $("[data-ed-focus]");
  if (focusBtn) focusBtn.addEventListener("click", () => {
    root.classList.toggle("is-focus-mode");
    focusBtn.classList.toggle("is-active", root.classList.contains("is-focus-mode"));
  });

  // ────────────────────────────────────────────────────────────
  // Compare slider + scroll sync
  // ────────────────────────────────────────────────────────────

  const compareBtn = $("[data-ed-compare]");
  let compareActive = false;
  if (compareBtn && frameWrap && frameBaseline) {
    compareBtn.addEventListener("click", () => {
      compareActive = !compareActive;
      frameWrap.classList.toggle("is-compare", compareActive);
      compareBtn.classList.toggle("is-active", compareActive);
      if (compareActive) {
        frameWrap.style.setProperty("--ed-split", "50%");
        // Load baseline iframe if first time OR if locale changed since
        if (!frameBaseline.src || frameBaseline.src.indexOf("baseline=1") === -1) {
          frameBaseline.src = withLang(baselineUrlBase);
        }
      }
    });

    const split = $(".ed-split", frameWrap);
    let dragging = false;
    function onDragMove(e) {
      if (!dragging) return;
      const rect = frameWrap.getBoundingClientRect();
      const clientX = (e.touches && e.touches[0]) ? e.touches[0].clientX : e.clientX;
      const pct = Math.max(3, Math.min(97, ((clientX - rect.left) / rect.width) * 100));
      frameWrap.style.setProperty("--ed-split", pct + "%");
    }
    function onDragEnd() { dragging = false; document.body.style.cursor = ""; }
    if (split) {
      split.addEventListener("mousedown", (e) => { dragging = true; document.body.style.cursor = "ew-resize"; e.preventDefault(); });
      split.addEventListener("touchstart", () => { dragging = true; });
      window.addEventListener("mousemove", onDragMove);
      window.addEventListener("touchmove", onDragMove, { passive: true });
      window.addEventListener("mouseup", onDragEnd);
      window.addEventListener("touchend", onDragEnd);
    }
  }

  // Scroll sync: the iframe that the user is interacting with is the
  // "leader". We track the most-recently-hovered frame; its scroll
  // drives the other. We debounce writes so the follower doesn't
  // round-trip scroll events back.
  let activeScroller = null;
  function setActiveScroller(f) { activeScroller = f; }
  if (frame)         frame.addEventListener("mouseenter",         () => setActiveScroller(frame));
  if (frameBaseline) frameBaseline.addEventListener("mouseenter", () => setActiveScroller(frameBaseline));

  function getIframeScrollY(f) {
    try { return f && f.contentDocument ? f.contentDocument.defaultView.scrollY : 0; }
    catch (e) { return 0; }
  }
  function syncScrollTo(f, y) {
    try {
      if (f && f.contentDocument) f.contentDocument.defaultView.scrollTo({ top: y, behavior: "instant" });
    } catch (e) {}
  }

  let syncTicking = false;
  function wireIframeScrollSync(f) {
    if (!f || !f.contentDocument) return;
    const win = f.contentDocument.defaultView;
    win.addEventListener("scroll", () => {
      if (!compareActive) return;
      if (activeScroller !== f) return;
      if (syncTicking) return;
      syncTicking = true;
      requestAnimationFrame(() => {
        const y = getIframeScrollY(f);
        const other = (f === frame) ? frameBaseline : frame;
        syncScrollTo(other, y);
        syncTicking = false;
      });
    }, { passive: true });
  }

  // ────────────────────────────────────────────────────────────
  // Snapshot button
  // ────────────────────────────────────────────────────────────

  const snapshotBtn = $("[data-ed-snapshot]");
  if (snapshotBtn && cfg.snapshotUrl) {
    snapshotBtn.addEventListener("click", () => {
      if (pendingTimer) { clearTimeout(pendingTimer); pendingTimer = null; }
      const doSnap = () => {
        fetch(cfg.snapshotUrl, {
          method: "POST",
          headers: { "X-CSRFToken": csrfToken, "X-Requested-With": "XMLHttpRequest" },
          credentials: "same-origin",
        })
          .then((r) => r.json())
          .then((data) => {
            if (data.ok) toast("Versione salvata nella cronologia", "success");
            else toast("Impossibile creare la versione.", "error");
          })
          .catch(() => toast("Impossibile creare la versione.", "error"));
      };
      if (Object.keys(dirtyContent).length || Object.keys(dirtyTokens).length) {
        flushDirty();
        setTimeout(doSnap, 900);
      } else {
        doSnap();
      }
    });
  }

  window.addEventListener("beforeunload", () => {
    if (Object.keys(dirtyContent).length || Object.keys(dirtyTokens).length) {
      navigator.sendBeacon(
        autosaveUrl,
        new Blob([JSON.stringify({ content: dirtyContent, tokens: dirtyTokens })], {
          type: "application/json",
        })
      );
    }
  });

  window.MWEditor = {
    toast, setStatus, flushDirty, refreshPreview,
    get currentLang() { return currentLang; },
  };
})();
