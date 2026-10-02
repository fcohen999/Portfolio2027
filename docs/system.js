// Shared behaviour for the v2 system. Everything here is progressive:
// without JS, tab panels stack, the rail is a plain list, images are links.

(function () {
  // ---- Tab viewers ----
  document.querySelectorAll('.tabs-viewer').forEach(function (viewer) {
    var tabs = Array.prototype.slice.call(viewer.querySelectorAll('[role="tab"]:not([aria-disabled="true"])'));
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on);
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); });
      t.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!d) return;
        e.preventDefault();
        select(tabs[(i + d + tabs.length) % tabs.length], true);
      });
    });
    select(tabs[0]);
  });

  // ---- Rail: current section, progress, running header ----
  var links = Array.prototype.slice.call(document.querySelectorAll('.rail a[href^="#"]'));
  var running = document.querySelector('.masthead [data-current]');
  var bar = document.querySelector('.rail .progress i');
  if (links.length) {
    var targets = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    var ticking = false;
    function update() {
      ticking = false;
      var line = window.innerHeight * 0.3;
      var current = -1;
      targets.forEach(function (el, i) { if (el && el.getBoundingClientRect().top <= line) current = i; });
      // a sub-entry implies its parent is current too
      links.forEach(function (a, i) {
        var on = i === current;
        var parentOn = current > -1 && links[current].closest('li li') && a.parentNode.contains(links[current]);
        a.setAttribute('aria-current', on || parentOn ? 'true' : 'false');
      });
      if (running) {
        var top = current > -1 ? links[current].closest('.rail > ol > li').querySelector('a') : null;
        running.textContent = top ? top.querySelector('span:last-child').textContent : '';
      }
      if (bar) {
        var body = document.querySelector('.content');
        var r = body.getBoundingClientRect();
        var p = Math.min(1, Math.max(0, (line - r.top) / r.height));
        bar.style.width = (p * 100).toFixed(1) + '%';
      }
      // keep the mobile strip's current item in view
      var cur = document.querySelector('.rail > ol > li > a[aria-current="true"]');
      var strip = document.querySelector('.rail > ol');
      if (cur && strip && strip.scrollWidth > strip.clientWidth) {
        var l = cur.offsetLeft - strip.offsetLeft;
        if (l < strip.scrollLeft || l + cur.offsetWidth > strip.scrollLeft + strip.clientWidth) strip.scrollLeft = l - 16;
      }
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  // ---- Lightbox: inspect any figure at full resolution ----
  var figImgs = document.querySelectorAll('.fig img, .tabs-viewer .panel img');
  if (!figImgs.length || !window.HTMLDialogElement) return;
  var dlg = document.createElement('dialog');
  dlg.className = 'lightbox';
  dlg.innerHTML =
    '<div class="lb-bar"><span class="lb-cap"></span><span class="lb-actions">' +
    '<button type="button" data-act="size">Actual size</button>' +
    '<button type="button" data-act="close">Close</button></span></div>' +
    '<div class="lb-stage"><img alt=""></div>';
  document.body.appendChild(dlg);
  var lbImg = dlg.querySelector('img');
  var lbCap = dlg.querySelector('.lb-cap');
  var sizeBtn = dlg.querySelector('[data-act="size"]');
  function setActual(on) {
    dlg.classList.toggle('actual', on);
    sizeBtn.textContent = on ? 'Fit to screen' : 'Actual size';
  }
  figImgs.forEach(function (img) {
    img.addEventListener('click', function () {
      lbImg.src = img.currentSrc || img.src;
      lbImg.alt = img.alt;
      // data-label is "<fig no.> — <title>"
      var parts = (img.getAttribute('data-label') || img.alt).split(' — ');
      lbCap.innerHTML = '';
      if (parts.length > 1) {
        var n = document.createElement('span'); n.className = 'num'; n.textContent = 'Fig. ' + parts.shift();
        lbCap.appendChild(n);
      }
      lbCap.appendChild(document.createTextNode(parts.join(' — ')));
      setActual(false);
      dlg.showModal();
    });
  });
  sizeBtn.addEventListener('click', function () { setActual(!dlg.classList.contains('actual')); });
  lbImg.addEventListener('click', function () { setActual(!dlg.classList.contains('actual')); });
  dlg.querySelector('[data-act="close"]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg.querySelector('.lb-stage')) dlg.close(); });
})();
