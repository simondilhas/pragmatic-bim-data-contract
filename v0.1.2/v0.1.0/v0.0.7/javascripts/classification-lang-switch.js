(function () {
  var STORAGE_KEY = "pbs-classification-lang";

  function setActiveLang(panel, lang) {
    panel.setAttribute("data-active-lang", lang);
    var buttons = panel.querySelectorAll(".pbs-lang-btn");
    buttons.forEach(function (button) {
      var isActive = button.getAttribute("data-lang") === lang;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", isActive ? "true" : "false");
    });
  }

  function initPanel(panel) {
    var defaultLang = panel.getAttribute("data-default-lang") || "en";
    var savedLang = null;
    try {
      savedLang = localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      savedLang = null;
    }

    var available = Array.prototype.map.call(
      panel.querySelectorAll(".pbs-lang-btn"),
      function (button) {
        return button.getAttribute("data-lang");
      }
    );
    var initialLang =
      savedLang && available.indexOf(savedLang) !== -1 ? savedLang : defaultLang;
    setActiveLang(panel, initialLang);

    panel.addEventListener("click", function (event) {
      var button = event.target.closest(".pbs-lang-btn");
      if (!button || !panel.contains(button)) {
        return;
      }
      var lang = button.getAttribute("data-lang");
      if (!lang) {
        return;
      }
      setActiveLang(panel, lang);
      try {
        localStorage.setItem(STORAGE_KEY, lang);
      } catch (e) {
        /* ignore storage errors */
      }
    });
  }

  function init() {
    document.querySelectorAll(".pbs-vocab-concepts").forEach(initPanel);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
