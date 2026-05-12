/* Working Diagnosis - site interactions
   Loaded at end of body in base.njk after pagefind-ui.js, so the DOM
   is fully parsed and PagefindUI is available when this runs. */
(function () {
  'use strict';

  // ---- Pagefind UI -----------------------------------------------------
  if (typeof PagefindUI !== 'undefined') {
    new PagefindUI({ element: '#search', showSubResults: true });
  }

  // ---- Search dropdown -------------------------------------------------
  var trigger  = document.getElementById('search-trigger');
  var dropdown = document.getElementById('search-dropdown');

  function isSearchOpen() {
    return dropdown && !dropdown.hidden;
  }

  function openSearch() {
    if (!dropdown) return;
    dropdown.hidden = false;
    (function focusInput() {
      var input = dropdown.querySelector('input[type="text"], input:not([type])');
      if (input) { input.focus(); }
      else { setTimeout(focusInput, 50); }
    })();
  }

  function closeSearch() {
    if (!dropdown) return;
    dropdown.hidden = true;
  }

  if (trigger) trigger.addEventListener('click', openSearch);

  // ---- Nav dropdowns ---------------------------------------------------
  var navDrops = document.querySelectorAll('.nav-drop');

  function closeAllNavDrops() {
    navDrops.forEach(function (d) { if (d.open) d.open = false; });
  }

  // Opening one closes the others
  navDrops.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      navDrops.forEach(function (other) { if (other !== d) other.open = false; });
    });
  });

  // ---- Global handlers (one keydown, one click) ------------------------
  document.addEventListener('keydown', function (e) {
    // Cmd/Ctrl-K toggles search
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      if (isSearchOpen()) closeSearch();
      else openSearch();
      return;
    }
    // Escape closes search and any open nav dropdown
    if (e.key === 'Escape') {
      if (isSearchOpen()) closeSearch();
      closeAllNavDrops();
    }
  });

  document.addEventListener('click', function (e) {
    // Close search if the click is outside both dropdown and trigger
    if (isSearchOpen()
        && !dropdown.contains(e.target)
        && (!trigger || !trigger.contains(e.target))) {
      closeSearch();
    }
    // Close any nav dropdown whose click is outside it
    navDrops.forEach(function (d) {
      if (d.open && !d.contains(e.target)) d.open = false;
    });
  });
})();
