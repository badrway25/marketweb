/* ============================================================================
 * MarketWeb — Live Media (premium video + logo marquee runtime)
 * ============================================================================
 *
 * Pairs with static/css/live-media.css.
 *
 * Responsibilities
 *   1. Lazy-boot any [data-lm-media="video"] block on first user click.
 *      Swaps the poster for a native HTML5 <video> with explicit controls.
 *      No autoplay, no invasive iframes, no third-party tracking surface.
 *   2. Duplicate the .lm-logo-marquee-track in place so the keyframe -50%
 *      translates a seamless loop. Hover-pause is pure CSS.
 *
 * Safe to load `defer`. Runs once on DOMContentLoaded.
 * Respects prefers-reduced-motion (skips marquee duplication, reveals the
 * full track in a static row instead).
 * ============================================================================ */

(function () {
  'use strict';

  function init() {
    setupVideos();
    setupLogoMarquees();
  }

  // --- 1. VIDEO -------------------------------------------------------------
  function setupVideos() {
    var blocks = document.querySelectorAll('[data-lm-media="video"]');
    if (!blocks.length) return;

    blocks.forEach(function (block) {
      var play = block.querySelector('.lm-video-play');
      if (!play) return;

      // The play button is the focusable interaction surface.
      play.addEventListener('click', function () {
        bootVideo(block);
      });

      // Keyboard: Enter/Space already trigger native button behavior; nothing
      // extra needed. Esc on a playing video pauses it for politeness.
      block.addEventListener('keydown', function (e) {
        if (e.key !== 'Escape') return;
        var v = block.querySelector('video');
        if (v && !v.paused) {
          v.pause();
          block.classList.remove('is-playing');
        }
      });
    });
  }

  function bootVideo(block) {
    if (block.classList.contains('is-playing')) return;
    var src    = block.getAttribute('data-lm-video-src') || '';
    var poster = block.getAttribute('data-lm-video-poster') || '';
    var loop   = block.getAttribute('data-lm-video-loop')   === 'true';
    var muted  = block.getAttribute('data-lm-video-muted')  === 'true';
    var auto   = block.getAttribute('data-lm-video-autoplay') === 'true'; // only honored when muted

    if (!src) return;

    // Build the <video>
    var v = block.querySelector('video');
    if (!v) {
      v = document.createElement('video');
      v.setAttribute('controls', '');
      v.setAttribute('controlslist', 'nodownload');
      v.setAttribute('playsinline', '');
      v.setAttribute('preload', 'metadata');
      if (poster) v.setAttribute('poster', poster);
      if (loop)   v.setAttribute('loop', '');
      if (muted)  v.setAttribute('muted', '');
      var s = document.createElement('source');
      s.src = src;
      // Best-effort type sniff from extension
      if (/\.webm(\?|$)/i.test(src))      s.type = 'video/webm';
      else if (/\.mp4(\?|$)/i.test(src))  s.type = 'video/mp4';
      v.appendChild(s);
      block.appendChild(v);
    }

    block.classList.add('is-playing');

    // Try to play. If the browser blocks (mobile / no-gesture / muted-required),
    // the native controls are still visible so the user can press play directly.
    var playPromise = v.play && v.play();
    if (playPromise && typeof playPromise.catch === 'function') {
      playPromise.catch(function () { /* user can press the native control */ });
    }

    // If this is meant as an ambient autoplay-muted loop, kick it once muted.
    if (auto && muted) {
      v.muted = true;
      try { v.play(); } catch (_) { /* swallow */ }
    }
  }

  // --- 2. LOGO MARQUEE ------------------------------------------------------
  function setupLogoMarquees() {
    var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var tracks = document.querySelectorAll('.lm-logo-marquee-track');
    if (!tracks.length) return;

    tracks.forEach(function (track) {
      // Reduced motion: leave the track static. The mask still fades the edges
      // so it still reads as a wordmark strip rather than an animated band.
      if (reduced) {
        track.style.animation = 'none';
        return;
      }
      if (track.getAttribute('data-lm-duplicated') === '1') return;
      var clone = track.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
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
