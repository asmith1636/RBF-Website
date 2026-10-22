// RBF Construction — small progressive enhancements (site works without JS)
(function () {
  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var head = document.querySelector('.site-header').getBoundingClientRect();
      nav.style.top = Math.max(0, head.bottom) + 'px';
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
  }

  // Before / after slider
  document.querySelectorAll('.ba').forEach(function (ba) {
    var input = ba.querySelector('input');
    var set = function () { ba.style.setProperty('--pos', input.value + '%'); };
    input.addEventListener('input', set);
    set();
  });

  // Gallery lightbox
  var box = document.querySelector('.lightbox');
  if (box && box.showModal) {
    var img = box.querySelector('img');
    var cap = box.querySelector('p');
    document.querySelectorAll('.gallery button').forEach(function (b) {
      b.addEventListener('click', function () {
        var i = b.querySelector('img');
        img.src = i.currentSrc || i.src;
        img.alt = i.alt;
        cap.textContent = b.dataset.caption || i.alt;
        box.showModal();
      });
    });
    box.addEventListener('click', function (e) {
      if (e.target === box || e.target.classList.contains('close')) box.close();
    });
  }

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -60px 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
