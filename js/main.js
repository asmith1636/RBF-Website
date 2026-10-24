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

  // Gallery filters
  document.querySelectorAll('.filters').forEach(function (bar) {
    var figs = bar.nextElementSibling.querySelectorAll('figure');
    bar.querySelectorAll('button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var f = btn.dataset.filter;
        bar.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        figs.forEach(function (fig) { fig.hidden = !(f === 'all' || fig.dataset.cat === f); });
      });
    });
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

  // ---- Lead tracking: events go to window.dataLayer (read by GA4/Tag Manager once installed)
  window.dataLayer = window.dataLayer || [];
  var track = function (event, detail) {
    var o = { event: event, page_path: location.pathname };
    for (var k in detail) o[k] = detail[k];
    window.dataLayer.push(o);
    if (typeof window.gtag === 'function') window.gtag('event', event, detail);
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    if (h.indexOf('tel:') === 0) track('phone_click', { link_text: a.textContent.trim() });
    else if (h.indexOf('mailto:') === 0) track('email_click', {});
    else if (h.indexOf('#quote') !== -1) track('bid_cta_click', { link_text: a.textContent.trim() });
  });

  // ---- Bid form: prefill from ?audience=&type= and record where the lead came from
  var form = document.querySelector('form.card-form');
  if (form) {
    var q = new URLSearchParams(location.search);
    ['audience', 'type'].forEach(function (key) {
      var v = q.get(key);
      var sel = form.querySelector(key === 'type' ? '#project_type' : '#audience');
      var opt = v && sel && sel.querySelector('option[data-key="' + v.replace(/[^a-z-]/g, '') + '"]');
      if (opt) sel.value = opt.value;
    });
    var setField = function (name, value) { var f = form.querySelector('input[name="' + name + '"]'); if (f) f.value = value; };
    var pageName = function (path) { return path === '/' ? 'Homepage' : path; };
    var store = function (k, v) { try { if (v) sessionStorage.setItem(k, v); return sessionStorage.getItem(k) || v || ''; } catch (err) { return v || ''; } };
    var camp = ['utm_source', 'utm_medium', 'utm_campaign'].map(function (k) { return q.get(k) ? k + '=' + q.get(k) : ''; }).filter(Boolean).join('&');
    var ref = document.referrer;
    var fromPage = ref && ref.indexOf(location.host) !== -1 ? new URL(ref).pathname : '';
    setField('_next', location.origin + '/thank-you');  // stay on the same domain (staging or production)
    var origin = store('rbf_referrer', '');
    var found = ['First page visited: ' + pageName(store('rbf_first_page', '') || location.pathname)];
    if (fromPage) found.push('Opened the form from: ' + pageName(fromPage));
    if (origin) found.push('Came from: ' + origin.replace(/^https?:\/\/(www\.)?/, '').replace(/\/$/, ''));
    var campaign = store('rbf_campaign', camp);
    if (campaign) found.push('Campaign: ' + campaign);
    setField('How They Found Us', found.join(' · '));
    form.addEventListener('submit', function () {
      setField('_replyto', (form.querySelector('#email') || {}).value || '');
      // leave unanswered optional fields out of the email
      form.querySelectorAll('input, select, textarea').forEach(function (f) { if (!f.value && f.name !== '_honey') f.disabled = true; });
      // save a copy in the RBF admin; the form still posts to FormSubmit for the email
      var kind = { '/get-a-quote': 'quote', '/bidding-list': 'sub', '/careers': 'job' }[location.pathname.replace(/\.html$/, '')];
      try { if (kind && navigator.sendBeacon) { var copy = new FormData(form); copy.append('_kind', kind); navigator.sendBeacon('/api/submit.php', copy); } } catch (err) { /* email still goes out */ }
      track('generate_lead_submit', { audience: (form.querySelector('#audience') || {}).value || '', project_type: (form.querySelector('#project_type') || {}).value || '' });
    });
    // coming back with the Back button: re-enable the fields
    window.addEventListener('pageshow', function () { form.querySelectorAll('[disabled]').forEach(function (f) { f.disabled = false; }); });
  }
  // remember first page / referrer / campaign of the visit for the bid form
  try {
    if (!sessionStorage.getItem('rbf_first_page')) sessionStorage.setItem('rbf_first_page', location.pathname);
    if (!sessionStorage.getItem('rbf_referrer') && document.referrer && document.referrer.indexOf(location.host) === -1 && document.referrer.indexOf('formsubmit.co') === -1) sessionStorage.setItem('rbf_referrer', document.referrer);
    var qs = new URLSearchParams(location.search);
    if (qs.get('utm_source')) sessionStorage.setItem('rbf_campaign', ['utm_source', 'utm_medium', 'utm_campaign'].map(function (k) { return qs.get(k) ? k + '=' + qs.get(k) : ''; }).filter(Boolean).join('&'));
  } catch (err) { /* storage unavailable: tracking fields stay empty */ }
  if (location.pathname === '/thank-you') track('generate_lead', {});

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
