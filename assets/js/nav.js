/* Mobile navigation: one compact menu button instead of a clipped link strip.
   Kept in its own file so both pages (home + CV) share the same behaviour. */
(function () {
  "use strict";
  var nav = document.querySelector(".nav");
  var btn = document.getElementById("nav-toggle");
  var links = document.getElementById("nav-links");
  if (!nav || !btn || !links) return;

  function setOpen(open) {
    nav.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  }

  btn.addEventListener("click", function () {
    setOpen(!nav.classList.contains("open"));
  });

  links.addEventListener("click", function (e) {
    if (e.target && e.target.closest && e.target.closest("a")) setOpen(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && nav.classList.contains("open")) {
      setOpen(false);
      btn.focus();
    }
  });

  var wide = window.matchMedia("(min-width: 621px)");
  function onChange() { if (wide.matches) setOpen(false); }
  if (wide.addEventListener) wide.addEventListener("change", onChange);
  else if (wide.addListener) wide.addListener(onChange);
})();
