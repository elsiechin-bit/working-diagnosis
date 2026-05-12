(function () {
  'use strict';

  var tocEl  = document.getElementById('page-toc');
  var bodyEl = document.querySelector('.topic-body');

  if (!tocEl || !bodyEl) return;

  var headings = Array.from(bodyEl.querySelectorAll('h2, h3'));

  // Need at least 2 headings to be worth showing
  if (headings.length < 2) {
    var wrapper = document.querySelector('.page-wrapper');
    if (wrapper) wrapper.classList.remove('has-toc');
    tocEl.style.display = 'none';
    return;
  }

  // Assign IDs to headings that don't already have one
  headings.forEach(function (h) {
    if (!h.id) {
      h.id = h.textContent
        .trim()
        .toLowerCase()
        .replace(/[^a-z0-9\s-]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-')
        .replace(/^-|-$/g, '');
    }
  });

  // Build the nav element
  var nav = document.createElement('nav');
  nav.className = 'toc-nav';
  nav.setAttribute('aria-label', 'On this page');

  var label = document.createElement('p');
  label.className = 'toc-heading';
  label.textContent = 'On this page';
  nav.appendChild(label);

  var list = document.createElement('ul');
  list.className = 'toc-list';

  headings.forEach(function (h) {
    var li = document.createElement('li');
    li.className = 'toc-item toc-item--' + h.tagName.toLowerCase();

    var a = document.createElement('a');
    a.className = 'toc-link';
    a.href = '#' + h.id;
    a.textContent = h.textContent.trim();

    li.appendChild(a);
    list.appendChild(li);
  });

  nav.appendChild(list);
  tocEl.appendChild(nav);

  // Scroll-highlight via IntersectionObserver
  var links = Array.from(list.querySelectorAll('.toc-link'));

  function setActive(id) {
    links.forEach(function (a) {
      a.classList.toggle('is-active', a.getAttribute('href') === '#' + id);
    });
  }

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          setActive(entry.target.id);
        }
      });
    }, {
      rootMargin: '-72px 0px -65% 0px'
    });

    headings.forEach(function (h) { observer.observe(h); });
  }

  // Default: first heading active on load
  if (headings.length > 0) setActive(headings[0].id);
})();
