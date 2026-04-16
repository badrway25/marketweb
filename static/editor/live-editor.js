/* Live Editor — Phase A.2 + A.2.1 + A.2.5 premium shell controller
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
 *
 * A.2.5 page-aware targeting (step 1):
 *  - Each sidebar group declares a `data-ed-page` slug ("home",
 *    "studio", … or "*" for chrome). When a field is focused and its
 *    page differs from the page currently loaded in the iframe, the
 *    iframe navigates to the right page FIRST; highlight/scroll runs
 *    only AFTER the load event, so the ring never lands on a stale DOM.
 *  - `currentPage` is re-synced from the iframe URL on every load, so
 *    in-iframe clicks (user navigating via the skin's nav) stay in
 *    sync without extra postMessage plumbing.
 *  - `refreshPreview()` now reloads the CURRENT page, not hardcoded
 *    home — autosave no longer yanks users back to the home route.
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
  // A.2.5 — page-aware targeting state
  //
  // `currentPage` tracks which page of the template the iframe is
  // showing RIGHT NOW. It starts from `cfg.initialPage` (server-side
  // guarantees the initial iframe src points there) and is kept in
  // sync with the iframe URL inside the `load` handler. Any sidebar
  // focus whose group declares a different `data-ed-page` triggers
  // a page-switch BEFORE the highlight lands.
  //
  // `pendingFocusActivation` holds the highlight request that needs
  // to fire *after* the next iframe load (the one caused by navigate
  // ToPage). Clearing it is the responsibility of the load handler —
  // the activation survives exactly one load cycle.
  // ────────────────────────────────────────────────────────────

  const previewBasePath = cfg.previewBasePath || "";
  const projectUuid     = cfg.projectUuid || "";
  const availablePages  = (cfg.availablePages || []).slice();
  let   currentPage     = cfg.initialPage || "home";
  let   pendingFocusActivation = null;

  function buildPageUrl(page, opts) {
    opts = opts || {};
    const p = page || currentPage || "home";
    let url = previewBasePath;
    if (p && p !== "home") url += p + "/";
    url += (url.indexOf("?") === -1 ? "?" : "&") + "project=" + encodeURIComponent(projectUuid);
    if (opts.baseline) url += "&baseline=1";
    url = withLang(url);
    if (opts.cachebust) url += (url.indexOf("?") === -1 ? "?" : "&") + "_t=" + Date.now();
    return url;
  }

  function pageFromIframeLocation(f) {
    try {
      const path = f && f.contentWindow && f.contentWindow.location.pathname;
      if (!path) return null;
      const m = path.match(/\/preview\/([^\/]+)\/?$/);
      if (!m) return "home";
      const slug = m[1];
      if (availablePages.indexOf(slug) !== -1) return slug;
      // Not a page slug (might be /preview/ trailing "/"-normalised) → home
      return "home";
    } catch (e) { return null; }
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

      // A.2.5: re-sync currentPage from the iframe's actual URL.
      // Covers both (a) our own navigatePreviewToPage and (b) user
      // clicks on the skin's nav links inside the iframe, so the next
      // autosave reload + focus routing stays accurate.
      const detected = pageFromIframeLocation(frame);
      if (detected) currentPage = detected;

      // If a focus on a field triggered a page switch, the activation
      // is deferred until this exact load. Consume it ONCE (scroll=true),
      // otherwise fall back to the A.2.4 behaviour: re-paint the last
      // highlight without scroll.
      if (pendingFocusActivation) {
        const { selector, label } = pendingFocusActivation;
        pendingFocusActivation = null;
        // Small delay lets the skin layout settle (web fonts, images)
        // so getBoundingClientRect lands on the final position.
        setTimeout(() => postHighlight(selector, label, true), 80);
      } else if (lastHighlight.selector) {
        setTimeout(() => postHighlight(lastHighlight.selector, lastHighlight.label, false), 80);
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
    // A.2.5: autosave reload must preserve the user's current page,
    // never yank them back to home.
    frame.src = previewBasePath
      ? buildPageUrl(currentPage, { cachebust: true })
      : (withLang(previewUrlBase) + (previewUrlBase.indexOf("?") === -1 ? "?" : "&") + "_t=" + Date.now());
  }

  function reloadBothFrames() {
    lastScroll = getIframeScrollY(frame) || 0;
    if (frame) {
      frame.src = previewBasePath
        ? buildPageUrl(currentPage, { cachebust: true })
        : (withLang(previewUrlBase) + (previewUrlBase.indexOf("?") === -1 ? "?" : "&") + "_t=" + Date.now());
    }
    if (frameBaseline && frameBaseline.src) {
      frameBaseline.src = previewBasePath
        ? buildPageUrl(currentPage, { baseline: true, cachebust: true })
        : (withLang(baselineUrlBase) + (baselineUrlBase.indexOf("?") === -1 ? "?" : "&") + "_t=" + Date.now());
    }
  }

  // A.2.5 — navigate the edited iframe to a specific page.
  // Returns true if a navigation was scheduled, false if already there
  // or the page is invalid. Callers that want a highlight post-load
  // MUST set `pendingFocusActivation` BEFORE calling this so the load
  // handler can consume it exactly once.
  function navigatePreviewToPage(page) {
    if (!frame || !previewBasePath) return false;
    if (!page || page === "*") return false;
    if (page !== "home" && availablePages.indexOf(page) === -1) return false;
    if (page === currentPage) return false;
    currentPage = page;
    // Fresh page → discard any preserved scroll from the previous page
    // (restoring an old Y on a new DOM is worse than landing at top).
    lastScroll = 0;
    // Discard the stale highlight record; if this navigation was
    // triggered by focus, pendingFocusActivation carries the new one.
    lastHighlight = { selector: "", label: "" };
    frame.src = buildPageUrl(page, { cachebust: true });
    return true;
  }

  // ────────────────────────────────────────────────────────────
  // Highlight postMessage — robust re-paint + idle hold
  // ────────────────────────────────────────────────────────────

  let highlightHoldTimer = null;

  // A.2.4: `scroll` is opt-in and per-activation. It is only true when
  // the user explicitly clicks/focuses a sidebar field (or reactivates
  // a different target). Autosave reload repaints, 5s idle clears,
  // group-head hover, and compare repaints all pass scroll=false so
  // the preview never chases the user.
  function postHighlight(selector, label, scroll) {
    lastHighlight = { selector: selector || "", label: label || "" };
    if (frame && frame.contentWindow) {
      frame.contentWindow.postMessage({
        source: "mw-editor",
        kind: "highlight",
        selector: selector || "",
        label: label || "",
        scroll: scroll === true,
      }, window.location.origin);
    }
    // Keep the highlight alive for a while so autosave reload (iframe
    // load event, ~300ms) does not visibly blink the overlay away.
    clearTimeout(highlightHoldTimer);
    if (selector) {
      highlightHoldTimer = setTimeout(() => {
        // Only clear if no sidebar field has focus
        if (!document.activeElement || !document.activeElement.closest(".ed-field")) {
          postHighlight("", "", false);
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

    // Highlight mapping: focus is the ONLY event that requests a scroll
    // (A.2.4 click/focus-driven policy). Blur does NOT clear — the 5s
    // idle timer inside postHighlight handles that cleanly while the
    // user is still typing into the field.
    //
    // A.2.5: if the field belongs to a different page than the one
    // currently shown in the iframe, we navigate FIRST and let the
    // iframe load handler consume `pendingFocusActivation` to paint
    // the highlight with scroll once the new DOM is ready.
    const group = input.closest(".ed-group");
    const region = group ? group.getAttribute("data-region") : "";
    const groupPage = group ? (group.getAttribute("data-ed-page") || "*") : "*";
    const label = input.closest(".ed-field")
                  ? (input.closest(".ed-field").getAttribute("data-ed-label") || "")
                  : "";
    input.addEventListener("focus", () => {
      if (groupPage && groupPage !== "*" && groupPage !== currentPage) {
        pendingFocusActivation = { selector: region, label: label };
        const ok = navigatePreviewToPage(groupPage);
        if (ok) return;
        // Fallthrough: navigation refused (e.g. unknown page) — still
        // paint on the current page so the user never loses feedback.
        pendingFocusActivation = null;
      }
      postHighlight(region, label, true);
    });

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

  // Group-head hover flashes the region — highlight only, NO scroll
  // (A.2.4: only field focus/click may scroll the preview).
  $$(".ed-group-head").forEach((btn) => {
    const group = btn.closest(".ed-group");
    const region = group ? group.getAttribute("data-region") : "";
    const label  = group ? (group.querySelector(".ed-glabel")?.textContent.trim() || "") : "";
    btn.addEventListener("mouseenter", () => {
      if (!document.activeElement || !document.activeElement.closest(".ed-field")) {
        postHighlight(region, label, false);
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

  // A.2.5 — command palette replaces the old inline filter. The
  // palette logic lives after the focus-handler wiring so it can
  // dispatch a synthetic focus on jump (triggering page-aware nav).

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
  // A.2.5 — Premium command palette
  //
  // Opens with ⌘K / Ctrl-K / `/` from anywhere (except while typing
  // into an editor input — `/` and `Ctrl-K` in inputs stay literal).
  // Clicking the sidebar trigger also opens it. The palette owns its
  // own <input>, so the sidebar trigger is purely a visual affordance.
  //
  // Index data: rendered as JSON in a <script> tag by the view; parsed
  // once at init. Ranking is deterministic, synchronous, token-based.
  // No fuzzy/Levenshtein on purpose — we control the labels + keywords.
  // ────────────────────────────────────────────────────────────

  const PALETTE_MAX_RESULTS = 40;
  const PALETTE_SUGGESTIONS = [
    { q: "hero",     label: "Home · Hero" },
    { q: "contatti", label: "Contatti" },
    { q: "colori",   label: "Colori e tipografia" },
    { q: "logo",     label: "Logo e brand" },
    { q: "email",    label: "Email" },
    { q: "studio",   label: "Chi siamo" },
  ];

  function normaliseText(s) {
    if (s == null) return "";
    // NFD + strip combining marks = accent-fold. Lowercase. Trim
    // punctuation to whitespace so "chi siamo" matches "chi-siamo".
    return String(s)
      .toLowerCase()
      .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-z0-9\s]+/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function buildPaletteIndex() {
    const script = document.getElementById("ed-palette-index");
    if (!script) return [];
    let data;
    try { data = JSON.parse(script.textContent || "[]"); }
    catch (e) { return []; }
    if (!Array.isArray(data)) return [];
    return data.map((row) => {
      const label = row.label || row.key || "";
      const help = row.help || "";
      const placeholder = row.placeholder || "";
      const kws = (row.keywords || []).join(" ");
      const pageLbl = row.page_label || "";
      const groupLbl = row.group_label || "";
      const subLbl = row.subgroup_label || "";
      const key = row.key || "";
      return {
        key:             key,
        kind:            row.kind || "content",
        label:           label,
        labelNorm:       normaliseText(label),
        help:            help,
        helpNorm:        normaliseText(help),
        placeholderNorm: normaliseText(placeholder),
        keywordsNorm:    normaliseText(kws),
        page:            row.page || "*",
        pageLabel:       pageLbl,
        pageLabelNorm:   normaliseText(pageLbl),
        groupId:         row.group_id || "",
        groupLabel:      groupLbl,
        groupLabelNorm:  normaliseText(groupLbl),
        subgroupLabel:   subLbl,
        subgroupNorm:    normaliseText(subLbl),
        keyNorm:         normaliseText(key),
        type:            row.type || "text",
        typeLabel:       row.type_label || "",
        icon:            row.icon || "bi-input-cursor",
      };
    });
  }

  // A.2.7 L3 — page-intent tuning.
  //
  // With 284 fields, a single generic token like "studio" used to
  // match `contatti.studio_label` (label contains "studio" → +140)
  // ahead of any real Studio-page field (page_label contains "studio"
  // → only +60). Two surgical boosts close the gap without reshaping
  // the ranking:
  //
  //   +200  when the whole query EQUALS the page_label  → "studio"
  //         pulls every Studio-page field to the top.
  //   + 60  when the whole query EQUALS the group_label → "brand",
  //         "contatti", "hero" pull their own group first.
  //
  // Both are exact-normalised matches, so a query of "studio legale"
  // gets no boost (it's not a page) and the existing per-token scoring
  // continues to work. The floor on `rankItems` is raised from >0 to
  // >=10 so pure help/placeholder whispers (+6/+3) stop polluting
  // long result lists — anything meaningful hits at least a keyNorm
  // (+10) or label-token (+35).
  function scoreItem(item, queryNorm, tokens) {
    if (!queryNorm) return 1; // empty query → keep, bucketed order
    let score = 0;
    // Whole-phrase boosts against the label first
    if (item.labelNorm === queryNorm) score += 1000;
    else if (item.labelNorm.startsWith(queryNorm)) score += 240;
    else if (item.labelNorm.indexOf(queryNorm) !== -1) score += 140;
    if (item.keywordsNorm.indexOf(queryNorm) !== -1) score += 90;
    if (item.pageLabelNorm === queryNorm) score += 200;
    else if (item.pageLabelNorm.indexOf(queryNorm) !== -1) score += 60;
    if (item.groupLabelNorm === queryNorm) score += 60;
    else if (item.groupLabelNorm.indexOf(queryNorm) !== -1) score += 60;
    // Per-token (so "contatti email" also works)
    for (let i = 0; i < tokens.length; i++) {
      const t = tokens[i];
      if (t.length < 2) continue;
      if (item.labelNorm.indexOf(t) !== -1) score += 35;
      if (item.keywordsNorm.indexOf(t) !== -1) score += 30;
      if (item.pageLabelNorm.indexOf(t) !== -1) score += 20;
      if (item.groupLabelNorm.indexOf(t) !== -1) score += 18;
      if (item.subgroupNorm.indexOf(t) !== -1) score += 12;
      if (item.keyNorm.indexOf(t) !== -1) score += 10;
      if (item.helpNorm.indexOf(t) !== -1) score += 6;
      if (item.placeholderNorm.indexOf(t) !== -1) score += 3;
    }
    return score;
  }

  const PALETTE_SCORE_FLOOR = 10;

  function rankItems(index, query) {
    const queryNorm = normaliseText(query);
    const tokens = queryNorm ? queryNorm.split(" ").filter(Boolean) : [];
    const hasQuery = queryNorm.length > 0;
    const scored = [];
    for (let i = 0; i < index.length; i++) {
      const s = scoreItem(index[i], queryNorm, tokens);
      // Empty query keeps its bucketed order; query runs get a floor so
      // help-only / placeholder-only noise (+6 / +3) is dropped.
      if (!hasQuery) { if (s > 0) scored.push({ item: index[i], score: s }); }
      else if (s >= PALETTE_SCORE_FLOOR) scored.push({ item: index[i], score: s });
    }
    scored.sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      return a.item.labelNorm < b.item.labelNorm ? -1 :
             a.item.labelNorm > b.item.labelNorm ?  1 : 0;
    });
    return scored.slice(0, PALETTE_MAX_RESULTS).map((s) => s.item);
  }

  function highlightMatch(text, queryNorm) {
    // Escape HTML first; then mark the matched run with <em>. We match
    // on the normalised (accent-fold) positions but substitute back on
    // the original string so casing/accents are preserved in output.
    if (!text) return "";
    const safe = text.replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    })[c]);
    if (!queryNorm) return safe;
    const norm = normaliseText(text);
    const idx = norm.indexOf(queryNorm);
    if (idx === -1) return safe;
    // Walk original string alongside normalised one to pick the slice.
    // Since NFD may expand the string, we approximate by re-normalising
    // per-char prefixes and stopping at idx / idx+len. For labels (short
    // strings) this is cheap.
    const qlen = queryNorm.length;
    let startOrig = -1, endOrig = -1;
    let acc = "";
    for (let i = 0; i < text.length; i++) {
      acc = normaliseText(text.slice(0, i + 1));
      if (startOrig === -1 && acc.length > idx) startOrig = i;
      if (acc.length >= idx + qlen) { endOrig = i + 1; break; }
    }
    if (startOrig === -1 || endOrig === -1) return safe;
    const pre  = text.slice(0, startOrig);
    const mid  = text.slice(startOrig, endOrig);
    const post = text.slice(endOrig);
    const esc = (s) => s.replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    })[c]);
    return esc(pre) + "<em>" + esc(mid) + "</em>" + esc(post);
  }

  const paletteIndex = buildPaletteIndex();
  const palette       = document.getElementById("ed-palette");
  const paletteInput  = document.getElementById("ed-palette-input");
  const paletteResults = document.getElementById("ed-palette-results");
  const paletteCount  = palette && palette.querySelector(".ed-palette-count");
  let paletteActiveIdx = 0;
  let paletteCurrentResults = [];
  let palettePreviouslyFocused = null;

  function renderPaletteResults() {
    if (!paletteResults || !paletteInput) return;
    const q = paletteInput.value;
    const qNorm = normaliseText(q);
    const items = rankItems(paletteIndex, q);
    paletteCurrentResults = items;

    if (!q) {
      // Empty state: suggestion chips + top-group overview.
      const chipsHtml = PALETTE_SUGGESTIONS.map((s) =>
        `<button type="button" class="ed-palette-chip" data-ed-chip="${s.q.replace(/"/g,"&quot;")}">${s.label}</button>`
      ).join("");
      paletteResults.innerHTML = `
        <div class="ed-palette-empty">
          <div class="ed-palette-empty-title">Salta al campo giusto in un lampo</div>
          <div class="ed-palette-empty-sub">Cerca per pagina, sezione, nome del campo o sinonimo.</div>
          <div class="ed-palette-chips">${chipsHtml}</div>
        </div>`;
      paletteActiveIdx = 0;
      if (paletteCount) paletteCount.textContent = "";
      // Wire chip buttons to seed a query.
      $$(".ed-palette-chip", paletteResults).forEach((chip) => {
        chip.addEventListener("click", () => {
          paletteInput.value = chip.getAttribute("data-ed-chip") || "";
          paletteInput.dispatchEvent(new Event("input", { bubbles: true }));
          paletteInput.focus();
        });
      });
      return;
    }

    if (!items.length) {
      paletteResults.innerHTML = `
        <div class="ed-palette-empty">
          <div class="ed-palette-empty-title">Nessun risultato per "${
            q.replace(/[&<>"']/g, (c) => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"})[c])
          }"</div>
          <div class="ed-palette-empty-sub">Prova con un termine più generico, oppure il nome di una pagina.</div>
        </div>`;
      paletteActiveIdx = 0;
      if (paletteCount) paletteCount.textContent = "0 risultati";
      return;
    }

    // Group results by page label (preserve input order within each
    // group so the top-scoring item stays first overall).
    const groupsInOrder = [];
    const groupMap = {};
    items.forEach((it, flatIdx) => {
      const pl = it.pageLabel || "Ovunque";
      if (!groupMap[pl]) {
        groupMap[pl] = [];
        groupsInOrder.push(pl);
      }
      groupMap[pl].push({ it: it, flatIdx: flatIdx });
    });

    let html = "";
    groupsInOrder.forEach((pl) => {
      const bucket = groupMap[pl];
      html += `<div class="ed-palette-group">
        <div class="ed-palette-grouplabel">${
          pl.replace(/[&<>"']/g, (c) => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"})[c])
        } <span class="count">${bucket.length}</span></div>`;
      bucket.forEach(({ it, flatIdx }) => {
        const labelHtml = highlightMatch(it.label, qNorm);
        const crumbParts = [];
        if (it.groupLabel) crumbParts.push(it.groupLabel);
        if (it.subgroupLabel) crumbParts.push(it.subgroupLabel);
        const crumbHtml = crumbParts
          .map((s) => s.replace(/[&<>"']/g, (c) => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"})[c]))
          .join(' <span class="sep">·</span> ');
        html += `
          <button type="button"
                  class="ed-palette-result"
                  role="option"
                  data-ed-result-index="${flatIdx}"
                  data-ed-key="${it.key.replace(/"/g, "&quot;")}"
                  data-ed-kind="${it.kind}">
            <i class="bi ${it.icon}" aria-hidden="true"></i>
            <div class="ed-palette-result-text">
              <span class="ed-palette-result-label">${labelHtml}</span>
              <span class="ed-palette-result-crumb">${crumbHtml}</span>
            </div>
            <span class="ed-palette-result-type">${it.typeLabel}</span>
          </button>`;
      });
      html += "</div>";
    });
    paletteResults.innerHTML = html;
    paletteActiveIdx = 0;
    updatePaletteActive();
    if (paletteCount) {
      paletteCount.textContent = items.length + (items.length === 1 ? " risultato" : " risultati");
    }
  }

  function updatePaletteActive() {
    if (!paletteResults) return;
    const rows = $$(".ed-palette-result", paletteResults);
    rows.forEach((r, i) => r.classList.toggle("is-active", i === paletteActiveIdx));
    const active = rows[paletteActiveIdx];
    if (active) active.scrollIntoView({ block: "nearest" });
  }

  function movePaletteActive(delta) {
    if (!paletteCurrentResults.length) return;
    const n = paletteCurrentResults.length;
    paletteActiveIdx = (paletteActiveIdx + delta + n) % n;
    updatePaletteActive();
  }

  function openPalette() {
    if (!palette) return;
    if (palette.classList.contains("is-open")) return;
    palettePreviouslyFocused = document.activeElement;
    palette.classList.add("is-open");
    palette.setAttribute("aria-hidden", "false");
    if (paletteInput) {
      paletteInput.value = "";
      renderPaletteResults();
      // Defer focus so the animation doesn't steal a tick.
      setTimeout(() => paletteInput.focus(), 0);
    }
  }

  function closePalette() {
    if (!palette) return;
    if (!palette.classList.contains("is-open")) return;
    palette.classList.remove("is-open");
    palette.setAttribute("aria-hidden", "true");
    if (palettePreviouslyFocused && typeof palettePreviouslyFocused.focus === "function") {
      try { palettePreviouslyFocused.focus(); } catch (e) {}
    }
  }

  function jumpToField(key, kind) {
    if (!key) return false;
    const selector = `[data-ed-field="${CSS.escape(key)}"][data-ed-kind="${CSS.escape(kind || "content")}"]`;
    const input = document.querySelector(selector);
    if (!input) return false;
    const group = input.closest(".ed-group");
    const field = input.closest(".ed-field");
    if (group) group.classList.add("is-open");
    if (field) {
      // One-shot pulse so the eye lands on the right row once the
      // accordion opens. Cleared after the animation finishes.
      field.classList.remove("is-just-jumped");
      void field.offsetWidth; // reflow, restart animation
      field.classList.add("is-just-jumped");
      setTimeout(() => field.classList.remove("is-just-jumped"), 950);
      field.scrollIntoView({ behavior: "smooth", block: "center" });
    }
    // A jump is claiming the sidebar — cancel any pending focus-restore
    // from closePalette() so the sidebar lands on the target instead of
    // scrolling back to wherever the user was before opening the palette.
    palettePreviouslyFocused = null;
    // Focus triggers the page-aware nav + highlight pipeline that was
    // wired in step 1. We defer a tick so scrollIntoView has settled.
    setTimeout(() => {
      try { input.focus({ preventScroll: true }); }
      catch (e) { input.focus(); }
    }, 120);
    return true;
  }

  if (palette && paletteInput && paletteResults) {
    // Platform hint for the keyboard chip ("⌘K" on Mac, "Ctrl K" on PC)
    const isMac = /Mac|iPad|iPhone/i.test(navigator.platform || navigator.userAgent || "");
    if (!isMac) document.body.classList.add("platform-pc");

    paletteInput.addEventListener("input", renderPaletteResults);

    paletteInput.addEventListener("keydown", (e) => {
      if (e.key === "ArrowDown") { e.preventDefault(); movePaletteActive(+1); }
      else if (e.key === "ArrowUp")   { e.preventDefault(); movePaletteActive(-1); }
      else if (e.key === "Enter") {
        e.preventDefault();
        const item = paletteCurrentResults[paletteActiveIdx];
        if (!item) return;
        const ok = jumpToField(item.key, item.kind);
        if (ok) closePalette();
        else toast("Impossibile aprire il campo richiesto.", "error");
      } else if (e.key === "Escape") {
        e.preventDefault();
        closePalette();
      }
    });

    // Click on a result row — delegated so dynamic content works
    paletteResults.addEventListener("click", (e) => {
      const row = e.target.closest(".ed-palette-result");
      if (!row) return;
      const key  = row.getAttribute("data-ed-key");
      const kind = row.getAttribute("data-ed-kind") || "content";
      const ok = jumpToField(key, kind);
      if (ok) closePalette();
    });

    // Hovering a result makes it the active one (keyboard + mouse parity)
    paletteResults.addEventListener("mousemove", (e) => {
      const row = e.target.closest(".ed-palette-result");
      if (!row) return;
      const i = parseInt(row.getAttribute("data-ed-result-index") || "-1", 10);
      if (i >= 0 && i !== paletteActiveIdx) {
        paletteActiveIdx = i;
        updatePaletteActive();
      }
    });

    // Close affordances
    $$("[data-ed-palette-close]", palette).forEach((el) => {
      el.addEventListener("click", closePalette);
    });
  }

  // Sidebar trigger button(s) → open palette
  $$("[data-ed-open-palette]").forEach((btn) => {
    btn.addEventListener("click", openPalette);
  });

  // Global shortcut: ⌘K / Ctrl-K everywhere, `/` outside inputs.
  window.addEventListener("keydown", (e) => {
    const isMetaK = (e.key === "k" || e.key === "K") && (e.metaKey || e.ctrlKey);
    if (isMetaK) {
      e.preventDefault();
      if (palette && palette.classList.contains("is-open")) closePalette();
      else openPalette();
      return;
    }
    if (e.key === "Escape" && palette && palette.classList.contains("is-open")) {
      e.preventDefault();
      closePalette();
      return;
    }
    if (e.key === "/") {
      const t = e.target;
      const inEditable = t && (
        t.tagName === "INPUT" || t.tagName === "TEXTAREA" ||
        t.tagName === "SELECT" || t.isContentEditable
      );
      if (inEditable) return;
      e.preventDefault();
      openPalette();
    }
  });

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
