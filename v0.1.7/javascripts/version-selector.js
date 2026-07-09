(function () {
  function currentVersionPrefix() {
    var parts = location.pathname.split("/").filter(Boolean);
    if (parts.length && (parts[0] === "latest" || /^v\d/.test(parts[0]))) {
      return parts[0];
    }
    return null;
  }

  function versionHref(version) {
    var suffix = location.pathname.replace(/^\/(latest|v[^/]+)/, "");
    if (!suffix || suffix === "/") {
      suffix = "/index.html";
    }
    return "/" + version + suffix + location.search + location.hash;
  }

  function createVersionSelector(versions, latest) {
    var header = document.querySelector(".md-header__inner");
    if (!header || header.querySelector(".pbs-version-selector")) {
      return;
    }

    var current = currentVersionPrefix() || latest;
    var wrapper = document.createElement("div");
    wrapper.className = "pbs-version-selector md-header__option";

    var label = document.createElement("label");
    label.className = "pbs-version-label";
    label.setAttribute("for", "pbs-version-select");
    label.textContent = "Version";

    var select = document.createElement("select");
    select.id = "pbs-version-select";
    select.className = "pbs-version-select";
    select.setAttribute("aria-label", "Select schema version");

    versions.forEach(function (version) {
      var option = document.createElement("option");
      option.value = version;
      option.textContent = version === latest ? version + " (latest)" : version;
      option.selected = version === current;
      select.appendChild(option);
    });

    select.addEventListener("change", function () {
      location.href = versionHref(select.value);
    });

    wrapper.appendChild(label);
    wrapper.appendChild(select);

    var searchButton = header.querySelector('label[for="__search"]');
    if (searchButton) {
      header.insertBefore(wrapper, searchButton);
    } else {
      header.appendChild(wrapper);
    }
  }

  function init() {
    fetch("/versions.json", { credentials: "same-origin" })
      .then(function (response) {
        if (!response.ok) {
          return null;
        }
        return response.json();
      })
      .then(function (data) {
        if (!data || !Array.isArray(data.versions) || !data.versions.length) {
          return;
        }
        createVersionSelector(data.versions, data.latest || data.versions[0]);
      })
      .catch(function () {
        /* no version metadata available locally */
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
