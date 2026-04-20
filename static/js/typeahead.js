/*
 * X.2 Commit 4 · Catalog typeahead + facet sync
 * ------------------------------------------------------------------
 * Vanilla JS · zero dependencies · debounce + AbortController.
 *
 * Contract:
 *  1. Any <input name="q"> inside a [data-typeahead-root] becomes a
 *     prefix-search typeahead for /templates/search/typeahead/.
 *  2. Facet checkboxes marked with data-facet + data-value write into
 *     a hidden aggregator input (name="cluster" / "style" / ...). The
 *     standard form submit picks those up as comma-separated params.
 *     This keeps the back-end URL contract stable + readable.
 *  3. All DOM work is idempotent — safe to re-run via turbolinks-
 *     style boosts or future SPA wrappers.
 *
 * The debounce is 180ms; stale requests are aborted via
 * AbortController so a slower connection never races an older reply
 * on top of the freshest keystroke.
 */
(function () {
  "use strict";

  var DEBOUNCE_MS = 180;
  var TYPEAHEAD_URL = "/templates/search/typeahead/";

  // ── Facet checkbox sync ───────────────────────────────────────
  //
  // Reads every [data-facet][data-value] checkbox inside the form
  // and aggregates the checked values into a comma-separated hidden
  // input named after the facet. Runs on DOMContentLoaded to prime
  // the hidden fields (so the back+forward cache is accurate), and
  // on every change event so user clicks flow through immediately.
  function syncFacetAggregators(form) {
    if (!form) return;
    var aggregators = {};
    var checkboxes = form.querySelectorAll("input[type=checkbox][data-facet]");
    checkboxes.forEach(function (cb) {
      var facet = cb.getAttribute("data-facet");
      var value = cb.getAttribute("data-value");
      if (!aggregators[facet]) aggregators[facet] = [];
      if (cb.checked && value) aggregators[facet].push(value);
    });
    Object.keys(aggregators).forEach(function (facet) {
      var hidden = form.querySelector(
        'input[type=hidden][name="' + facet + '"]'
      );
      if (hidden) hidden.value = aggregators[facet].join(",");
    });
  }

  function bindFacetSync() {
    var form = document.querySelector(".mw-catalog-layout");
    if (!form) return;
    syncFacetAggregators(form);
    form.addEventListener("change", function (e) {
      if (e.target && e.target.matches("input[type=checkbox][data-facet]")) {
        syncFacetAggregators(form);
      }
    });
  }

  // ── Typeahead ─────────────────────────────────────────────────

  function debounce(fn, wait) {
    var t;
    return function debounced() {
      var ctx = this, args = arguments;
      clearTimeout(t);
      t = setTimeout(function () { fn.apply(ctx, args); }, wait);
    };
  }

  function escapeHtml(s) {
    if (s == null) return "";
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function buildPanel() {
    var panel = document.createElement("div");
    panel.className = "mw-typeahead-panel";
    panel.setAttribute("role", "listbox");
    panel.setAttribute("aria-live", "polite");
    return panel;
  }

  function renderPayload(panel, payload) {
    var html = "";
    var hasAny = false;

    function renderGroup(title, items, itemHtml) {
      if (!items || !items.length) return;
      hasAny = true;
      html +=
        '<div class="mw-typeahead-group-title">' +
        escapeHtml(title) +
        "</div>";
      items.forEach(function (it) {
        html += itemHtml(it);
      });
    }

    renderGroup("Template", payload.templates, function (t) {
      return (
        '<a class="mw-typeahead-item" role="option" href="' +
        escapeHtml(t.detail_url) +
        '">' +
        escapeHtml(t.name) +
        (t.cluster
          ? "<small>" + escapeHtml(t.cluster) + "</small>"
          : "") +
        "</a>"
      );
    });
    renderGroup("Professioni", payload.clusters, function (c) {
      return (
        '<a class="mw-typeahead-item" role="option" href="' +
        escapeHtml(c.detail_url) +
        '">' +
        escapeHtml(c.name) +
        "</a>"
      );
    });
    renderGroup("Per ruolo", payload.roles, function (r) {
      return (
        '<a class="mw-typeahead-item" role="option" href="' +
        escapeHtml(r.detail_url) +
        '">' +
        escapeHtml(r.label) +
        "</a>"
      );
    });

    if (!hasAny) {
      html =
        '<div class="mw-typeahead-empty">Nessun risultato. Prova un\'altra parola chiave.</div>';
    }

    panel.innerHTML = html;
    panel.setAttribute("data-open", "1");
  }

  function closePanel(panel) {
    panel.removeAttribute("data-open");
    panel.innerHTML = "";
  }

  function bindTypeahead() {
    var inputs = document.querySelectorAll("[data-typeahead-root] input[name='q']");
    inputs.forEach(function (input) {
      var root = input.closest("[data-typeahead-root]");
      if (!root) return;
      // Mark the root so CSS knows to position the panel.
      root.classList.add("mw-typeahead");
      var panel = buildPanel();
      root.appendChild(panel);

      var ctrl = null;

      var fetchSuggestions = debounce(function () {
        var q = input.value.trim();
        if (q.length < 2) {
          closePanel(panel);
          return;
        }
        if (ctrl) ctrl.abort();
        ctrl = new AbortController();
        fetch(
          TYPEAHEAD_URL + "?q=" + encodeURIComponent(q) + "&limit=6",
          { signal: ctrl.signal, headers: { "Accept": "application/json" } }
        )
          .then(function (r) { return r.json(); })
          .then(function (payload) { renderPayload(panel, payload); })
          .catch(function (err) {
            if (err && err.name === "AbortError") return;
            closePanel(panel);
          });
      }, DEBOUNCE_MS);

      input.addEventListener("input", fetchSuggestions);
      input.addEventListener("focus", fetchSuggestions);
      input.addEventListener("blur", function () {
        // Let a click land on a panel item before closing.
        setTimeout(function () { closePanel(panel); }, 140);
      });
      input.addEventListener("keydown", function (e) {
        if (e.key === "Escape") closePanel(panel);
      });
    });
  }

  // ── Boot ──────────────────────────────────────────────────────
  function boot() {
    bindFacetSync();
    bindTypeahead();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
