/* sideline.no: the header's shadow once scrolled, and the phone menu (Esc, a tap outside or a link
   closes it; Tab stays inside; the page behind does not scroll). Same behaviour as spons.sideline.no. */
(function () {
  var d = document, root = d.documentElement;
  var bar = d.querySelector(".sitebar");
  function onScroll() { if (bar) bar.classList.toggle("is-scrolled", window.scrollY > 4); }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  var menu = d.getElementById("sitemenu-wrap"), panel = d.getElementById("sitemenu");
  var toggle = d.querySelector("[data-menu-toggle]");
  if (!menu || !panel || !toggle) return;
  function focusables() { return Array.prototype.slice.call(panel.querySelectorAll("a[href], button")); }
  function open() {
    menu.hidden = false; root.classList.add("menu-open"); toggle.setAttribute("aria-expanded", "true");
    var f = focusables(); if (f[0]) f[0].focus();
  }
  function close() {
    if (menu.hidden) return;
    menu.hidden = true; root.classList.remove("menu-open"); toggle.setAttribute("aria-expanded", "false"); toggle.focus();
  }
  toggle.addEventListener("click", function () { menu.hidden ? open() : close(); });
  menu.addEventListener("click", function (e) {
    if (e.target === menu || e.target.closest("[data-menu-close]") || e.target.closest("a[href]")) close();
  });
  d.addEventListener("keydown", function (e) {
    if (menu.hidden) return;
    if (e.key === "Escape") { close(); return; }
    if (e.key !== "Tab") return;
    var f = focusables(); if (!f.length) return;
    if (e.shiftKey && d.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && d.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  });
})();
