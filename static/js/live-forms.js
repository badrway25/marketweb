/* ============================================================================
 * MarketWeb — Live Forms runtime
 * ============================================================================
 *
 * Progressive-enhancement for live-forms primitives:
 *
 *   1. Custom listbox (.lf-select)
 *        Upgrades a real <select> into a role="combobox" trigger + a
 *        role="listbox" panel. Keyboard complete (↑ ↓ Home End Enter
 *        Space Esc Tab typeahead). ARIA correct. Native remains the
 *        source of truth for form submission.
 *
 *   2. File upload (.lf-upload)
 *        Wires the drop zone label, click opens native picker,
 *        shows file chips with size + remove. Drag-over state.
 *
 * Mobile / touch
 * --------------
 * On coarse pointers (touch, no hover) we keep the native <select> UI
 * because the platform picker is superior. The visual style of the
 * native select is kept consistent via CSS.
 *
 * Zero dependencies. IIFE + feature detection. Safe to load globally.
 * ============================================================================ */

(function () {
  'use strict';

  var isTouch = (function () {
    try {
      return window.matchMedia &&
             window.matchMedia('(hover: none) and (pointer: coarse)').matches;
    } catch (e) { return false; }
  })();

  /* ------------------------------------------------------------------------
   * 1. CUSTOM LISTBOX
   * ---------------------------------------------------------------------- */

  function enhanceSelect(wrapper) {
    var select = wrapper.querySelector('select');
    if (!select || wrapper.classList.contains('is-enhanced')) return;
    if (isTouch) return;   // keep native on touch devices

    var selectId = select.id || ('lf-sel-' + Math.random().toString(36).slice(2, 8));
    select.id = selectId;

    var listboxId = selectId + '-listbox';
    var placeholder = wrapper.getAttribute('data-lf-placeholder') || '';
    var label = wrapper.getAttribute('data-lf-label') || '';

    // Build trigger button
    var trigger = document.createElement('button');
    trigger.type = 'button';
    trigger.className = 'lf-select-trigger';
    trigger.setAttribute('role', 'combobox');
    trigger.setAttribute('aria-haspopup', 'listbox');
    trigger.setAttribute('aria-expanded', 'false');
    trigger.setAttribute('aria-controls', listboxId);
    if (label) trigger.setAttribute('aria-label', label);
    trigger.innerHTML = '<span class="lf-select-value"></span>' +
                        '<svg class="lf-select-caret" viewBox="0 0 10 6" aria-hidden="true">' +
                          '<path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>' +
                        '</svg>';

    // Build listbox
    var listbox = document.createElement('ul');
    listbox.className = 'lf-select-listbox';
    listbox.setAttribute('role', 'listbox');
    listbox.id = listboxId;
    listbox.tabIndex = -1;

    var options = Array.prototype.slice.call(select.options);
    var activeIndex = -1;

    options.forEach(function (opt, i) {
      var li = document.createElement('li');
      li.setAttribute('role', 'option');
      li.id = selectId + '-opt-' + i;
      li.textContent = opt.textContent;
      li.dataset.index = String(i);
      if (opt.disabled) li.setAttribute('aria-disabled', 'true');
      if (opt.selected && !isPlaceholderOption(opt)) li.setAttribute('aria-selected', 'true');
      li.addEventListener('click', function () { choose(i); close(); trigger.focus(); });
      li.addEventListener('mouseenter', function () { setActive(i); });
      listbox.appendChild(li);
    });

    wrapper.appendChild(trigger);
    wrapper.appendChild(listbox);
    wrapper.classList.add('is-enhanced');

    // Initial value
    var initialIndex = select.selectedIndex;
    if (initialIndex >= 0 && !isPlaceholderOption(options[initialIndex])) {
      setValueDisplay(options[initialIndex].textContent, false);
    } else {
      setValueDisplay(placeholder || (options[0] && options[0].textContent) || '', true);
    }

    // Keyboard + open/close
    trigger.addEventListener('click', toggle);
    trigger.addEventListener('keydown', onTriggerKey);
    document.addEventListener('click', onDocClick);
    document.addEventListener('keydown', onDocKey);

    function isPlaceholderOption(opt) {
      if (!opt) return false;
      var v = (opt.value || '').trim();
      return v === '' || opt.disabled;
    }

    function setValueDisplay(text, isPh) {
      var valueEl = trigger.querySelector('.lf-select-value');
      valueEl.textContent = text || '';
      valueEl.classList.toggle('is-placeholder', !!isPh);
    }

    function open() {
      if (wrapper.classList.contains('is-open')) return;
      wrapper.classList.add('is-open');
      trigger.setAttribute('aria-expanded', 'true');
      var idx = select.selectedIndex;
      setActive(idx >= 0 ? idx : 0);
      scrollActiveIntoView();
    }
    function close() {
      wrapper.classList.remove('is-open');
      trigger.setAttribute('aria-expanded', 'false');
      clearActive();
    }
    function toggle() {
      if (wrapper.classList.contains('is-open')) close();
      else open();
    }
    function choose(i) {
      if (i < 0 || i >= options.length) return;
      if (options[i].disabled) return;
      select.selectedIndex = i;
      // Update list aria-selected
      Array.prototype.forEach.call(listbox.children, function (li, j) {
        if (j === i && !isPlaceholderOption(options[j])) li.setAttribute('aria-selected', 'true');
        else li.removeAttribute('aria-selected');
      });
      // Fire native change event for any listener (Analytics, etc.)
      var evt;
      try { evt = new Event('change', { bubbles: true }); }
      catch (e) { evt = document.createEvent('Event'); evt.initEvent('change', true, false); }
      select.dispatchEvent(evt);
      setValueDisplay(options[i].textContent, isPlaceholderOption(options[i]));
    }
    function setActive(i) {
      clearActive();
      if (i < 0 || i >= options.length) return;
      activeIndex = i;
      var li = listbox.children[i];
      if (!li) return;
      li.classList.add('is-active');
      trigger.setAttribute('aria-activedescendant', li.id);
    }
    function clearActive() {
      Array.prototype.forEach.call(listbox.children, function (li) { li.classList.remove('is-active'); });
      activeIndex = -1;
      trigger.removeAttribute('aria-activedescendant');
    }
    function scrollActiveIntoView() {
      if (activeIndex < 0) return;
      var li = listbox.children[activeIndex];
      if (!li) return;
      var top = li.offsetTop, bottom = top + li.offsetHeight;
      if (top < listbox.scrollTop) listbox.scrollTop = top;
      else if (bottom > listbox.scrollTop + listbox.clientHeight) listbox.scrollTop = bottom - listbox.clientHeight;
    }
    function moveActive(delta) {
      if (!wrapper.classList.contains('is-open')) { open(); return; }
      var next = activeIndex < 0 ? (select.selectedIndex >= 0 ? select.selectedIndex : 0) : activeIndex + delta;
      if (next < 0) next = 0;
      if (next > options.length - 1) next = options.length - 1;
      // skip disabled
      while (next >= 0 && next < options.length && options[next].disabled) {
        next += delta > 0 ? 1 : -1;
      }
      if (next < 0 || next > options.length - 1) return;
      setActive(next);
      scrollActiveIntoView();
    }

    // typeahead buffer
    var typeBuf = '', typeTimer = null;
    function typeahead(ch) {
      typeBuf += ch.toLowerCase();
      if (typeTimer) clearTimeout(typeTimer);
      typeTimer = setTimeout(function () { typeBuf = ''; }, 600);
      for (var i = 0; i < options.length; i++) {
        if (options[i].disabled) continue;
        var t = (options[i].textContent || '').toLowerCase();
        if (t.indexOf(typeBuf) === 0) {
          if (wrapper.classList.contains('is-open')) { setActive(i); scrollActiveIntoView(); }
          else choose(i);
          break;
        }
      }
    }

    function onTriggerKey(e) {
      var k = e.key;
      if (k === 'ArrowDown' || k === 'Down') { e.preventDefault(); moveActive(1); }
      else if (k === 'ArrowUp' || k === 'Up') { e.preventDefault(); moveActive(-1); }
      else if (k === 'Home') { e.preventDefault(); open(); setActive(0); scrollActiveIntoView(); }
      else if (k === 'End') { e.preventDefault(); open(); setActive(options.length - 1); scrollActiveIntoView(); }
      else if (k === 'Enter' || k === ' ') {
        if (wrapper.classList.contains('is-open')) { e.preventDefault(); if (activeIndex >= 0) choose(activeIndex); close(); }
        else { e.preventDefault(); open(); }
      }
      else if (k === 'Escape' || k === 'Esc') { if (wrapper.classList.contains('is-open')) { e.preventDefault(); close(); } }
      else if (k === 'Tab') { close(); }
      else if (k.length === 1 && !e.ctrlKey && !e.metaKey && !e.altKey) { typeahead(k); }
    }

    function onDocClick(e) {
      if (!wrapper.classList.contains('is-open')) return;
      if (!wrapper.contains(e.target)) close();
    }
    function onDocKey(e) {
      if ((e.key === 'Escape' || e.key === 'Esc') && wrapper.classList.contains('is-open')) close();
    }
  }

  function enhanceSelects(scope) {
    var root = scope || document;
    Array.prototype.forEach.call(root.querySelectorAll('.lf-select'), enhanceSelect);
  }


  /* ------------------------------------------------------------------------
   * 2. FILE UPLOAD
   * ---------------------------------------------------------------------- */

  function formatSize(bytes) {
    if (!bytes || isNaN(bytes)) return '';
    var KB = bytes / 1024;
    if (KB < 1024) return Math.round(KB) + ' KB';
    var MB = KB / 1024;
    return MB.toFixed(MB >= 10 ? 0 : 1) + ' MB';
  }

  function enhanceUpload(wrapper) {
    if (wrapper.classList.contains('is-enhanced')) return;
    var input = wrapper.querySelector('input[type="file"]');
    var zone = wrapper.querySelector('.lf-upload-zone');
    var list = wrapper.querySelector('.lf-upload-list');
    if (!input || !zone) return;
    if (!list) {
      list = document.createElement('div');
      list.className = 'lf-upload-list';
      wrapper.appendChild(list);
    }
    wrapper.classList.add('is-enhanced');

    // Keep a DataTransfer-backed file list so we can remove individual
    // files (FileList itself is read-only). Fallback: full clear.
    var dt = null;
    try { dt = new DataTransfer(); } catch (e) { dt = null; }

    zone.addEventListener('click', function () { input.click(); });
    zone.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); input.click(); }
    });
    if (!zone.hasAttribute('tabindex')) zone.setAttribute('tabindex', '0');
    if (!zone.hasAttribute('role')) zone.setAttribute('role', 'button');
    if (!zone.hasAttribute('aria-label')) {
      var primary = zone.querySelector('.lf-upload-primary');
      if (primary) zone.setAttribute('aria-label', primary.textContent);
    }

    input.addEventListener('change', function () { render(); });

    ['dragenter', 'dragover'].forEach(function (ev) {
      zone.addEventListener(ev, function (e) { e.preventDefault(); wrapper.classList.add('is-dragging'); });
    });
    ['dragleave', 'drop'].forEach(function (ev) {
      zone.addEventListener(ev, function (e) { e.preventDefault(); wrapper.classList.remove('is-dragging'); });
    });
    zone.addEventListener('drop', function (e) {
      var files = e.dataTransfer && e.dataTransfer.files;
      if (!files || !files.length) return;
      if (dt) {
        // merge existing + new, honoring `multiple` attribute
        if (input.multiple) {
          Array.prototype.forEach.call(input.files || [], function (f) { dt.items.add(f); });
          Array.prototype.forEach.call(files, function (f) { dt.items.add(f); });
        } else {
          dt.items.add(files[0]);
        }
        input.files = dt.files;
      } else {
        try { input.files = files; } catch (err) { /* legacy browser: ignored */ }
      }
      render();
    });

    function render() {
      list.innerHTML = '';
      var files = input.files || [];
      if (!files.length) return;
      if (dt) { dt = new DataTransfer(); Array.prototype.forEach.call(files, function (f) { dt.items.add(f); }); }
      Array.prototype.forEach.call(files, function (file, idx) {
        var chip = document.createElement('span');
        chip.className = 'lf-upload-chip';
        var name = document.createElement('span'); name.className = 'name'; name.textContent = file.name;
        var size = document.createElement('span'); size.className = 'size'; size.textContent = formatSize(file.size);
        var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'remove';
        btn.setAttribute('aria-label', 'Rimuovi ' + file.name);
        btn.textContent = '×';
        btn.addEventListener('click', function (e) {
          e.stopPropagation();
          if (dt) {
            dt = new DataTransfer();
            Array.prototype.forEach.call(input.files, function (f, j) { if (j !== idx) dt.items.add(f); });
            input.files = dt.files;
          } else {
            input.value = '';
          }
          render();
        });
        chip.appendChild(name); chip.appendChild(size); chip.appendChild(btn);
        list.appendChild(chip);
      });
    }
  }

  function enhanceUploads(scope) {
    var root = scope || document;
    Array.prototype.forEach.call(root.querySelectorAll('.lf-upload'), enhanceUpload);
  }


  /* ------------------------------------------------------------------------
   * Bootstrap
   * ---------------------------------------------------------------------- */

  function boot() {
    enhanceSelects();
    enhanceUploads();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else { boot(); }

  window.LiveForms = { enhanceSelects: enhanceSelects, enhanceUploads: enhanceUploads };
})();
