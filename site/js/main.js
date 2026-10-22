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

  // Hero slideshow
  var hero = document.querySelector('.hero-slides');
  if (hero) {
    var slides = hero.querySelectorAll('.slide');
    var dots = hero.querySelectorAll('.dot');
    var slideCap = hero.querySelector('.slide-cap');
    var cur = 0, timer = null;
    var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var show = function (n) {
      cur = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) {
        s.classList.toggle('is-active', i === cur);
        s.setAttribute('aria-hidden', i === cur ? 'false' : 'true');
        if (i === cur) { var im = s.querySelector('img'); if (im.loading === 'lazy') im.loading = 'eager'; }
      });
      dots.forEach(function (d, i) { d.classList.toggle('is-active', i === cur); });
      if (slideCap) slideCap.textContent = slides[cur].dataset.caption;
      // warm up the next slide's image
      var nx = slides[(cur + 1) % slides.length].querySelector('img');
      if (nx.loading === 'lazy') nx.loading = 'eager';
    };
    var play = function () { if (!still) { stop(); timer = setInterval(function () { show(cur + 1); }, 6000); } };
    var stop = function () { if (timer) clearInterval(timer); timer = null; };
    hero.querySelector('.next').addEventListener('click', function () { show(cur + 1); play(); });
    hero.querySelector('.prev').addEventListener('click', function () { show(cur - 1); play(); });
    dots.forEach(function (d, i) { d.addEventListener('click', function () { show(i); play(); }); });
    hero.addEventListener('mouseenter', stop);
    hero.addEventListener('mouseleave', play);
    hero.addEventListener('focusin', stop);
    hero.addEventListener('focusout', play);
    var x0 = null;
    hero.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    hero.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) { show(cur + (dx < 0 ? 1 : -1)); play(); }
      x0 = null;
    });
    document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else play(); });
    show(0);
    play();
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
