/**
 * MarketWeb — Main JavaScript
 * Navbar scroll, mobile menu, and micro-interactions
 */

(function () {
  'use strict';

  // --- Navbar scroll effect ---
  const navbar = document.getElementById('mw-navbar');
  if (navbar) {
    const SCROLL_THRESHOLD = 20;
    let ticking = false;

    function updateNavbar() {
      if (window.scrollY > SCROLL_THRESHOLD) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(updateNavbar);
        ticking = true;
      }
    }, { passive: true });

    // Run on load in case page is already scrolled
    updateNavbar();
  }


  // --- Mobile menu ---
  const menuToggle = document.getElementById('mw-menu-toggle');
  const menuClose = document.getElementById('mw-menu-close');
  const mobileMenu = document.getElementById('mw-mobile-menu');
  const mobileOverlay = document.getElementById('mw-mobile-overlay');

  function openMobileMenu() {
    if (mobileMenu) mobileMenu.classList.add('show');
    if (mobileOverlay) mobileOverlay.classList.add('active');
    if (menuToggle) menuToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileMenu() {
    if (mobileMenu) mobileMenu.classList.remove('show');
    if (mobileOverlay) mobileOverlay.classList.remove('active');
    if (menuToggle) menuToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (menuToggle) menuToggle.addEventListener('click', openMobileMenu);
  if (menuClose) menuClose.addEventListener('click', closeMobileMenu);
  if (mobileOverlay) mobileOverlay.addEventListener('click', closeMobileMenu);

  // Close on Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && mobileMenu && mobileMenu.classList.contains('show')) {
      closeMobileMenu();
    }
  });

  // Close mobile menu on window resize to desktop
  window.addEventListener('resize', function () {
    if (window.innerWidth >= 992 && mobileMenu && mobileMenu.classList.contains('show')) {
      closeMobileMenu();
    }
  });

})();
