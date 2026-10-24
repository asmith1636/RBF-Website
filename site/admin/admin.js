// RBF admin conveniences. Everything still works without this script.
(function () {
  // "select all" in a list
  document.querySelectorAll('[data-all]').forEach(function (all) {
    var boxes = all.form.querySelectorAll('input[name="ids[]"]');
    all.addEventListener('change', function () { boxes.forEach(function (b) { b.checked = all.checked; }); });
  });

  // filters apply as soon as a choice changes
  document.querySelectorAll('form.filters select, form.filters input[type=date]').forEach(function (el) {
    el.addEventListener('change', function () { el.form.submit(); });
  });

  // bulk delete: tick the confirm box for them after asking
  document.querySelectorAll('form.bulk').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      var n = form.querySelectorAll('input[name="ids[]"]:checked').length;
      if (form.bulk.value === 'delete' && n) {
        if (!window.confirm('Permanently delete ' + n + ' record' + (n > 1 ? 's' : '') + ' and their notes?')) { e.preventDefault(); return; }
        form.confirm.checked = true;
      }
    });
  });

  // warn before leaving an edit form with unsaved changes
  document.querySelectorAll('form.cols').forEach(function (form) {
    var dirty = false;
    form.addEventListener('input', function () { dirty = true; });
    form.addEventListener('submit', function () { dirty = false; });
    window.addEventListener('beforeunload', function (e) { if (dirty) { e.preventDefault(); e.returnValue = ''; } });
  });
})();
