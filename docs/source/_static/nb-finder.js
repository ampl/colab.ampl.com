/*
 * Notebook finder for the AMPL Model Colaboratory home page.
 *
 * Adds search and filtering on top of the static notebook list rendered by
 * scripts/index.py. The static list stays the source of the markup; this script
 * only hides, shows and reorders its entries using the metadata in
 * _static/notebooks.json (written by docs/source/conf.py from the notebook
 * headers and docs/model-catalog.csv). Without JavaScript, or if the index
 * fails to load, the full list is shown.
 */
(function () {
  "use strict";

  const SCRIPT_URL = document.currentScript ? document.currentScript.src : document.baseURI;

  // Filter dropdowns, in display order. With mode "any", picking several values
  // matches notebooks with any of them; with mode "all", notebooks need every
  // selected value. Different filters always narrow each other down.
  const FACETS = [
    { field: "domains", label: "Domain", param: "domain", icon: "globe", mode: "any" },
    { field: "model_types", label: "Model type", param: "type", icon: "layers", mode: "any" },
    {
      field: "levels",
      label: "Level",
      param: "level",
      icon: "cap",
      mode: "any",
      order: ["Quick Start", "Lecture", "Case Study", "Industry Prototype"],
    },
    { field: "modules", label: "Solvers", param: "solver", icon: "cpu", mode: "any" },
    { field: "tags", label: "Tags", param: "tag", icon: "tag", mode: "all" },
    { field: "algorithms", label: "Algorithm", param: "algorithm", icon: "branch", mode: "any" },
    { field: "authors", label: "Authors", param: "author", icon: "user", mode: "any" },
  ];
  const MENU_SEARCH_MIN = 8; // show a search box in menus with at least this many options

  const ICONS = {
    globe: '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
    layers:
      '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    cap: '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    cpu: '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2M15 20v2M2 15h2M2 9h2M20 15h2M20 9h2M9 2v2M9 20v2"/>',
    tag: '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r="1"/>',
    branch: '<path d="M6 3v12"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
    user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    chevron: '<path d="m6 9 6 6 6-6"/>',
    x: '<path d="M18 6 6 18M6 6l12 12"/>',
  };

  function init() {
    const root = document.getElementById("nb-finder");
    if (!root) return;
    // notebooks.json sits next to this script in _static/, whatever the page's folder
    const src = root.getAttribute("data-index") || new URL("notebooks.json", SCRIPT_URL).href;
    fetch(src)
      .then((res) => {
        if (!res.ok) throw new Error(res.status + " " + res.statusText);
        return res.json();
      })
      .then((notebooks) => setup(root, notebooks))
      .catch((err) => console.warn("nb-finder: search index unavailable", err));
  }

  function fold(text) {
    return String(text || "")
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .toLowerCase();
  }

  function el(tag, attrs, children) {
    const node = document.createElement(tag);
    for (const [key, value] of Object.entries(attrs || {})) {
      if (value === false || value == null) continue;
      if (key === "text") node.textContent = value;
      else if (key === "class") node.className = value;
      else node.setAttribute(key, value === true ? "" : value);
    }
    for (const child of children || []) node.appendChild(child);
    return node;
  }

  function icon(name, cls) {
    const span = el("span", { class: "nb-finder__icon" + (cls ? " " + cls : ""), "aria-hidden": "true" });
    span.innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
      'stroke-linecap="round" stroke-linejoin="round">' + ICONS[name] + "</svg>";
    return span;
  }

  function countBy(items, keyFn) {
    const counts = new Map();
    for (const item of items) {
      for (const key of keyFn(item)) counts.set(key, (counts.get(key) || 0) + 1);
    }
    return counts;
  }

  function rank(order, value) {
    const index = order.indexOf(value);
    return index === -1 ? order.length : index;
  }

  // Pair each notebook with its rendered <section> via its GitHub badge, which
  // is the first GitHub link in the entry (descriptions may link to other
  // notebooks). Titles with markup can break the notebook page link, so that
  // is only a fallback.
  function findSections(root) {
    const sections = [...root.parentElement.children].filter(
      (node) => node !== root && (node.tagName === "SECTION" || node.classList.contains("section"))
    );
    const sectionByKey = new Map();
    for (const section of sections) {
      const hrefs = [...section.querySelectorAll("a[href]")].map((a) => a.getAttribute("href"));
      for (const href of hrefs) {
        const github = href.match(/^https:\/\/github\.com\/ampl\/colab\.ampl\.com\/blob\/[^/]+\/(.+\.ipynb)$/);
        if (github) {
          sectionByKey.set("path:" + github[1], section);
          break;
        }
      }
      for (const href of hrefs) {
        const page = href.match(/notebooks\/([^/#?]+)\.html/);
        if (page && page[1] !== "index") {
          sectionByKey.set("slug:" + page[1], section);
          break;
        }
      }
    }
    return (nb) => sectionByKey.get("path:" + nb.path) || sectionByKey.get("slug:" + nb.slug);
  }

  // Show the catalog classification under each entry's title
  function addMeta(item) {
    const parts = [...item.domains, ...item.subdomains, ...item.model_types, ...item.levels];
    const heading = item.section.querySelector("h1, h2, h3, h4, h5, h6");
    if (!parts.length || !heading || item.section.querySelector(".nb-finder__meta")) return;
    heading.after(
      el(
        "p",
        { class: "nb-finder__meta" },
        parts.map((text) => el("span", { class: "nb-finder__pill", text }))
      )
    );
  }

  // Links to author pages in the Authors page list and its sidebar navigation
  function findAuthorLinks(authorPages) {
    const links = document.querySelectorAll(
      "article .toctree-wrapper a[href], .bd-sidebar-primary .bd-docs-nav a[href]"
    );
    const entries = [];
    for (const link of links) {
      const page = link.getAttribute("href").split(/[?#]/)[0].split("/").pop().replace(/\.html$/, "");
      if (!authorPages.has(page)) continue;
      const text = link.textContent.trim();
      const match = text.match(/^(.*?)\s*\((\d+) notebooks?\)$/);
      entries.push({
        link,
        li: link.closest("li"),
        page,
        text,
        href: link.getAttribute("href").split(/[?#]/)[0],
        name: match ? match[1] : text,
        total: match ? Number(match[2]) : 0,
      });
    }
    return entries;
  }

  function setup(root, notebooks) {
    // "authors": filter the list of authors on the Authors page (sidebar menu only)
    const authorsMode = root.dataset.mode === "authors";
    const sectionFor = authorsMode ? () => null : findSections(root);
    const items = notebooks
      .map((nb, order) => {
        const item = { order, section: sectionFor(nb) };
        for (const field of [...FACETS.map((f) => f.field), "subdomains", "subjects", "author_pages"])
          item[field] = nb[field] || [];
        const catalog = [
          ...item.domains,
          ...item.subdomains,
          ...item.subjects,
          ...item.model_types,
          ...item.levels,
          ...item.algorithms,
        ];
        item.fields = {
          title: fold(nb.title),
          tags: fold(item.tags.join(" ") + " " + item.tags.join(" ").replace(/-/g, " ")),
          modules: fold(item.modules.join(" ")),
          catalog: fold(catalog.join(" ")),
          authors: fold(item.authors.join(" ")),
          description: fold(nb.description),
        };
        return item;
      })
      .filter((item) => authorsMode || item.section);
    if (!items.length) return;

    const authorPages = new Set(items.flatMap((item) => item.author_pages));
    const authorLinks = authorsMode ? findAuthorLinks(authorPages) : [];
    if (authorsMode && !authorLinks.length) return;
    if (!authorsMode) {
      items.forEach(addMeta);
      // Each notebook's entry in the theme's "On this page" navigation
      for (const item of items) {
        const link = item.section.id
          ? document.querySelector(`.bd-sidebar-secondary a[href="#${CSS.escape(item.section.id)}"]`)
          : null;
        item.tocEntry = link?.closest("li") || null;
      }
      setupPageToc();
    }

    const total = authorsMode ? new Set(authorLinks.map((entry) => entry.page)).size : items.length;
    const facets = FACETS.map((facet) => {
      const counts = countBy(items, (item) => item[facet.field]);
      const values = [...counts.keys()].sort(
        (a, b) => counts.get(b) - counts.get(a) || a.localeCompare(b)
      );
      if (facet.order) values.sort((a, b) => rank(facet.order, a) - rank(facet.order, b));
      // Values from all notebooks, so filters carried over from another page are kept
      const everywhere = new Set(notebooks.flatMap((nb) => nb[facet.field] || []));
      return { ...facet, values, known: new Set(values), everywhere, selected: new Set() };
    }).filter((facet) => facet.values.length);

    const state = { q: "" };
    readUrl();

    // ---- Controls -------------------------------------------------------
    const search = el("input", {
      type: "search",
      id: "nb-finder-q",
      class: "nb-finder__search",
      placeholder: "Search by title, description, domain, subject, tag, solver or author",
      autocomplete: "off",
      "aria-label": "Search notebooks",
    });
    search.value = state.q;

    const bar = el("div", { class: "nb-finder__bar", role: "toolbar", "aria-label": "Filters" });
    const activeRow = el("div", { class: "nb-finder__active", "aria-label": "Active filters" });
    const status = el("p", { class: "nb-finder__status", "aria-live": "polite" });
    const clear = el("button", { type: "button", class: "nb-finder__clear", text: "Clear all" });
    const empty = el("p", {
      class: "nb-finder__empty",
      hidden: true,
      text: "No notebooks match these filters. Try removing a filter or searching for a broader term.",
    });

    let openFacet = null; // the open dropdown (panel layout only)
    let ready = false; // set after the initial render

    for (const facet of facets) buildDropdown(facet);

    // The search box and filters sit in the page's left sidebar on wide screens
    // (where it stays in view while scrolling) and in the panel above the list
    // otherwise; the result count and active filters always stay above the list.
    const controls = el("div", { class: "nb-finder__controls" }, [
      el("div", { class: "nb-finder__searchbox" }, [icon("search", "nb-finder__search-icon"), search]),
      bar,
    ]);
    const panel = el("div", { class: "nb-finder__panel" }, [
      el("div", { class: "nb-finder__footer" }, [activeRow, el("div", { class: "nb-finder__summary" }, [status, clear])]),
    ]);
    const sideBox = el("div", { class: "sidebar-primary-item nb-finder-side" }, [
      el("p", { class: "nb-finder-side__title", text: authorsMode ? "Filter authors" : "Filter notebooks" }),
    ]);
    const sidebarSlot = document.querySelector(".bd-sidebar-primary .sidebar-primary-items__start");
    const wide = window.matchMedia("(min-width: 960px)");
    let inSidebar = false;

    if (authorsMode && sidebarSlot) {
      // Only the sidebar menu here (on small screens it lives in the theme's drawer);
      // the result count and "Clear all" sit under its title
      sideBox.appendChild(el("div", { class: "nb-finder__summary nb-finder-side__summary" }, [status, clear]));
    } else {
      root.appendChild(panel);
      root.appendChild(empty);
      root.hidden = false;
    }
    applyLayout();
    wide.addEventListener("change", applyLayout);

    function applyLayout() {
      closeMenu();
      inSidebar = Boolean(sidebarSlot) && (authorsMode || wide.matches);
      controls.classList.toggle("is-sidebar", inSidebar);
      root.classList.toggle("nb-finder--sidebar", inSidebar);
      if (inSidebar) {
        sideBox.appendChild(controls);
        // Right after "Search the docs" (and before the section navigation, if any)
        const searchItem = [...sidebarSlot.children].find((child) =>
          child.querySelector(".search-button-field, .bd-search, form")
        );
        if (searchItem) searchItem.after(sideBox);
        else sidebarSlot.prepend(sideBox);
      } else {
        panel.prepend(controls);
        sideBox.remove();
      }
      for (const facet of facets) {
        const expanded = inSidebar && facet.expanded;
        facet.menu.hidden = !expanded;
        facet.toggle.setAttribute("aria-expanded", String(expanded));
        facet.toggle.classList.toggle("is-open", expanded);
      }
    }

    // In the sidebar, bring the (changed) results into view when they are off screen
    function revealResults() {
      if (!inSidebar || authorsMode) return;
      const rect = root.getBoundingClientRect();
      if (rect.top > window.innerHeight - 160 || rect.bottom < 0) {
        const smooth = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        root.scrollIntoView({ behavior: smooth ? "smooth" : "auto", block: "start" });
      }
    }

    function buildDropdown(facet) {
      const id = "nb-finder-menu-" + facet.param;
      facet.badge = el("span", { class: "nb-finder__badge", hidden: true });
      facet.toggle = el(
        "button",
        {
          type: "button",
          class: "nb-finder__toggle",
          "aria-expanded": "false",
          "aria-controls": id,
          "aria-haspopup": "true",
        },
        [
          icon(facet.icon),
          el("span", { class: "nb-finder__toggle-label", text: facet.label }),
          facet.badge,
          icon("chevron", "nb-finder__chevron"),
        ]
      );

      facet.options = new Map();
      const list = el("div", { class: "nb-finder__options", role: "group", "aria-label": facet.label });
      for (const value of facet.values) {
        const box = el("input", { type: "checkbox", class: "nb-finder__check" });
        const count = el("span", { class: "nb-finder__count" });
        const option = el("label", { class: "nb-finder__option" }, [
          box,
          el("span", { class: "nb-finder__option-name", text: value }),
          count,
        ]);
        box.addEventListener("change", () => {
          if (box.checked) facet.selected.add(value);
          else facet.selected.delete(value);
          update();
        });
        facet.options.set(value, { option, box, count, name: fold(value) });
        list.appendChild(option);
      }

      const head = [];
      if (facet.values.length >= MENU_SEARCH_MIN) {
        facet.filter = el("input", {
          type: "search",
          class: "nb-finder__menu-search",
          placeholder: `Find ${facet.label.toLowerCase()}… (${facet.values.length})`,
          autocomplete: "off",
          "aria-label": `Find ${facet.label.toLowerCase()}`,
        });
        facet.filter.addEventListener("input", () => filterOptions(facet));
        head.push(facet.filter);
      }
      if (facet.mode === "all") {
        head.push(el("p", { class: "nb-finder__hint", text: "Shows notebooks that have all selected tags" }));
      }
      const noMatch = el("p", { class: "nb-finder__no-options", hidden: true, text: "No matching options" });
      facet.noMatch = noMatch;
      const reset = el("button", { type: "button", class: "nb-finder__menu-clear", text: "Clear" });
      reset.addEventListener("click", () => {
        facet.selected.clear();
        update();
      });
      const done = el("button", { type: "button", class: "nb-finder__menu-done", text: "Done" });
      done.addEventListener("click", () => closeMenu(true));

      facet.menu = el("div", { class: "nb-finder__menu", id, hidden: true }, [
        ...head,
        list,
        noMatch,
        el("div", { class: "nb-finder__menu-footer" }, [reset, done]),
      ]);
      // Sidebar sections start collapsed, except those with filters already chosen
      facet.expanded = facet.selected.size > 0;
      facet.toggle.addEventListener("click", () => {
        if (inSidebar) {
          facet.expanded = !facet.expanded;
          facet.menu.hidden = !facet.expanded;
          facet.toggle.setAttribute("aria-expanded", String(facet.expanded));
          facet.toggle.classList.toggle("is-open", facet.expanded);
        } else if (openFacet === facet) closeMenu();
        else openMenu(facet);
      });
      bar.appendChild(el("div", { class: "nb-finder__dropdown" }, [facet.toggle, facet.menu]));
    }

    function filterOptions(facet) {
      const query = fold(facet.filter ? facet.filter.value : "").trim();
      let shown = 0;
      for (const { option, name } of facet.options.values()) {
        const visible = !query || name.includes(query);
        option.hidden = !visible;
        if (visible) shown++;
      }
      facet.noMatch.hidden = shown > 0;
    }

    function openMenu(facet) {
      closeMenu();
      openFacet = facet;
      facet.menu.hidden = false;
      facet.toggle.setAttribute("aria-expanded", "true");
      facet.toggle.classList.add("is-open");
      // Keep the menu inside the viewport on narrow screens
      facet.menu.style.left = "";
      const rect = facet.menu.getBoundingClientRect();
      const overflow = rect.right - (document.documentElement.clientWidth - 8);
      if (overflow > 0) facet.menu.style.left = `${Math.max(-rect.left + 8, -overflow)}px`;
      (facet.filter || facet.menu.querySelector("input"))?.focus({ preventScroll: true });
    }

    function closeMenu(restoreFocus) {
      if (!openFacet) return;
      const facet = openFacet;
      openFacet = null;
      facet.menu.hidden = true;
      facet.toggle.setAttribute("aria-expanded", "false");
      facet.toggle.classList.remove("is-open");
      if (facet.filter && facet.filter.value) {
        facet.filter.value = "";
        filterOptions(facet);
      }
      if (restoreFocus) facet.toggle.focus();
    }

    document.addEventListener("click", (event) => {
      if (openFacet && !openFacet.toggle.parentElement.contains(event.target)) closeMenu();
    });

    // ---- Filtering ------------------------------------------------------
    function queryTokens() {
      return fold(state.q).split(/\s+/).filter(Boolean);
    }

    // Returns a relevance score, or 0 when the notebook does not match every token
    function scoreText(item, tokens) {
      let score = 1;
      for (const token of tokens) {
        const f = item.fields;
        if (f.title.includes(token)) score += 4;
        else if (f.tags.includes(token) || f.modules.includes(token)) score += 3;
        else if (f.catalog.includes(token) || f.authors.includes(token)) score += 2;
        else if (f.description.includes(token)) score += 1;
        else return 0;
      }
      return score;
    }

    // skip: a facet to leave out, to count what picking one of its values would give
    function matches(item, tokens, skip) {
      if (tokens.length && !scoreText(item, tokens)) return false;
      for (const facet of facets) {
        if (facet === skip || !facet.selected.size) continue;
        const values = item[facet.field];
        const ok =
          facet.mode === "all"
            ? [...facet.selected].every((value) => values.includes(value))
            : values.some((value) => facet.selected.has(value));
        if (!ok) return false;
      }
      return true;
    }

    function renderFacets(tokens, results) {
      for (const facet of facets) {
        // "any" counts ignore the facet's own selection; "all" counts show what would remain
        const base = facet.mode === "all" ? results : items.filter((item) => matches(item, tokens, facet));
        const live = countBy(base, (item) => item[facet.field]);
        for (const [value, parts] of facet.options) {
          const n = live.get(value) || 0;
          const checked = facet.selected.has(value);
          parts.box.checked = checked;
          parts.count.textContent = String(n);
          parts.option.classList.toggle("is-empty", n === 0 && !checked);
          parts.option.classList.toggle("is-checked", checked);
        }
        const size = facet.selected.size;
        facet.badge.hidden = !size;
        facet.badge.textContent = String(size);
        facet.toggle.classList.toggle("is-active", size > 0);
        facet.menu.classList.toggle("has-selection", size > 0);
        facet.toggle.setAttribute(
          "aria-label",
          size ? `${facet.label}, ${size} selected` : facet.label
        );
      }
    }

    function renderActive() {
      const chips = [];
      for (const facet of facets) {
        for (const value of facet.selected) {
          const remove = el(
            "button",
            { type: "button", class: "nb-finder__chip", "aria-label": `Remove ${facet.label}: ${value}` },
            [
              icon(facet.icon),
              el("span", { text: value }),
              icon("x", "nb-finder__chip-x"),
            ]
          );
          remove.addEventListener("click", () => {
            facet.selected.delete(value);
            update();
          });
          chips.push(remove);
        }
      }
      activeRow.replaceChildren(...chips);
      activeRow.hidden = !chips.length;
    }

    function update() {
      const tokens = queryTokens();
      const results = items.filter((item) => matches(item, tokens));
      const filtered = tokens.length || facets.some((facet) => facet.selected.size);
      const shown = authorsMode ? updateAuthors(results, filtered) : updateNotebooks(results, tokens);

      renderFacets(tokens, results);
      renderActive();
      const noun = authorsMode ? "authors" : "notebooks";
      status.replaceChildren(
        ...(filtered
          ? [el("strong", { text: String(shown) }), document.createTextNode(` of ${total} ${noun}`)]
          : [el("strong", { text: String(total) }), document.createTextNode(` ${noun}`)])
      );
      clear.hidden = !filtered;
      empty.hidden = authorsMode || results.length > 0;
      writeUrl();
      if (ready) revealResults();
    }

    function updateNotebooks(results, tokens) {
      const matched = new Set(results);
      for (const item of items) {
        item.section.classList.toggle("nb-finder-hidden", !matched.has(item));
        item.tocEntry?.classList.toggle("nb-finder-hidden", !matched.has(item));
      }
      // Rank by relevance while searching; otherwise keep the alphabetical order
      const ordered = tokens.length
        ? [...results].sort((a, b) => scoreText(b, tokens) - scoreText(a, tokens) || a.order - b.order)
        : items;
      let anchor = root;
      for (const item of ordered) {
        if (anchor.nextElementSibling !== item.section) anchor.after(item.section);
        anchor = item.section;
        // Keep "On this page" in the same order as the list
        item.tocEntry?.parentElement.appendChild(item.tocEntry);
      }
      return results.length;
    }

    // Authors page: show the authors with matching notebooks, and how many match
    function updateAuthors(results, filtered) {
      const counts = countBy(results, (item) => item.author_pages);
      for (const entry of authorLinks) {
        const n = counts.get(entry.page) || 0;
        entry.li?.classList.toggle("nb-finder-hidden", Boolean(filtered) && n === 0);
        entry.link.textContent = filtered
          ? `${entry.name} (${n} of ${entry.total} notebook${entry.total === 1 ? "" : "s"})`
          : entry.text;
        // The author's page opens with the same filters applied
        const query = filterParams().toString();
        entry.link.setAttribute("href", entry.href + (query ? "?" + query : ""));
      }
      return [...counts.keys()].filter((page) => authorPages.has(page)).length;
    }

    // ---- URL state ------------------------------------------------------
    function readUrl() {
      const params = new URLSearchParams(window.location.search);
      state.q = params.get("q") || "";
      for (const facet of facets) {
        for (const value of params.getAll(facet.param).flatMap((v) => v.split(","))) {
          if (!facet.known.has(value) && !facet.everywhere.has(value)) continue;
          facet.selected.add(value);
          if (!facet.known.has(value)) {
            facet.known.add(value);
            facet.values.push(value);
          }
        }
      }
    }

    // The current search and filters as URL parameters (other parameters kept)
    function filterParams() {
      const params = new URLSearchParams(window.location.search);
      for (const key of ["q", ...FACETS.map((facet) => facet.param)]) params.delete(key);
      if (state.q.trim()) params.set("q", state.q.trim());
      for (const facet of facets)
        for (const value of facet.selected) params.append(facet.param, value);
      return params;
    }

    function writeUrl() {
      const query = filterParams().toString();
      const url = window.location.pathname + (query ? "?" + query : "") + window.location.hash;
      window.history.replaceState(null, "", url);
    }

    // ---- Events ---------------------------------------------------------
    search.addEventListener("input", () => {
      state.q = search.value;
      update();
    });
    clear.addEventListener("click", () => {
      state.q = search.value = "";
      for (const facet of facets) facet.selected.clear();
      update();
      search.focus();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && openFacet) {
        event.preventDefault();
        closeMenu(true);
        return;
      }
      const target = event.target;
      const typing = target.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(target.tagName);
      if (event.key === "/" && !typing && !event.ctrlKey && !event.metaKey && !event.altKey) {
        event.preventDefault();
        search.focus();
      }
    });

    update();
    ready = true;
  }

  // With 124 notebooks, "On this page" is long: stretch the right sidebar to the
  // window edge (the theme centers the page at a maximum width), hide its
  // scrollbar, and scroll it along with the page so the entry highlighted by
  // the theme's scrollspy stays in view with a few entries of context above it
  const TOC_CONTEXT = 5;

  function setupPageToc() {
    const toc = document.querySelector(".bd-sidebar-secondary");
    const page = document.querySelector(".bd-container__inner");
    const nav = toc && toc.querySelector(".bd-toc-nav");
    if (!toc || !page || !nav) return;
    toc.classList.add("nb-finder-toc");

    const fit = () => {
      toc.style.removeProperty("--nbf-toc-extend");
      const gutter = document.documentElement.clientWidth - page.getBoundingClientRect().right;
      const visible = getComputedStyle(toc).display !== "none";
      toc.style.setProperty("--nbf-toc-extend", `${visible ? Math.max(0, Math.floor(gutter)) : 0}px`);
    };
    fit();
    window.addEventListener("resize", fit);

    let pending = false;
    let lastTarget = null;
    const follow = () => {
      pending = false;
      const active = [...nav.querySelectorAll("li.active")].pop();
      const entries = active
        ? [...active.parentElement.children].filter((li) => !li.classList.contains("nb-finder-hidden"))
        : [];
      const index = entries.indexOf(active);
      // Top-level entries (e.g. "Contents") keep the column at the top
      const target = index > 0 ? entries[Math.max(0, index - TOC_CONTEXT)] : null;
      if (target === lastTarget) return;
      lastTarget = target;
      const top = target
        ? target.getBoundingClientRect().top - toc.getBoundingClientRect().top + toc.scrollTop
        : 0;
      const smooth = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      toc.scrollTo({ top: Math.max(0, top), behavior: smooth ? "smooth" : "auto" });
    };
    new MutationObserver(() => {
      if (!pending) {
        pending = true;
        requestAnimationFrame(follow);
      }
    }).observe(nav, { subtree: true, attributes: true, attributeFilter: ["class"] });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
