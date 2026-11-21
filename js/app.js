(function () {
  "use strict";

  // Change this one value when the site name is decided.
  const SITE_NAME = "SiteName";

  const app = document.getElementById("app");
  const CATS = Object.fromEntries(window.CATEGORIES.map((c) => [c.id, c]));
  const EVENTS = Object.fromEntries(window.EVENTS.map((e) => [e.id, e]));
  const CONTENT = window.CONTENT || {};

  const LEVELS = [
    { id: "easy", name: "Easy", blurb: "Core vocabulary and fundamentals. Good for a first pass.", color: "#16a34a", bars: 1 },
    { id: "medium", name: "Medium", blurb: "Applying concepts and connecting ideas across chapters.", color: "#f59e0b", bars: 2 },
    { id: "hard", name: "Hard", blurb: "Competition-level detail, close distractors, multi-step reasoning.", color: "#dc2626", bars: 3 },
  ];

  // ---------- helpers ----------
  const esc = (s) =>
    String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

  const store = {
    get(key, fallback) {
      try { const v = localStorage.getItem(key); return v == null ? fallback : JSON.parse(v); } catch { return fallback; }
    },
    set(key, val) {
      try { localStorage.setItem(key, JSON.stringify(val)); } catch { /* storage unavailable */ }
    },
  };

  const icon = {
    book: '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg>',
    test: '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    quiz: '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>',
    cards: '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="15" height="14" rx="2"/><path d="M7 2h13a2 2 0 0 1 2 2v12"/></svg>',
    guide: '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4h6a1 1 0 0 1 1 1v1H8V5a1 1 0 0 1 1-1z"/><path d="M16 5h2a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h2"/><path d="M8.5 12.5l2 2 4-4"/><path d="M8 18h8"/></svg>',
    arrow: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    left: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>',
    right: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>',
    search: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>',
    shuffle: '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/></svg>',
  };

  function crumbs(items) {
    return (
      '<nav class="breadcrumbs" aria-label="Breadcrumb">' +
      items
        .map((it, i) =>
          (i ? '<span class="sep">/</span>' : "") + (it.href ? `<a href="${it.href}">${esc(it.label)}</a>` : `<span>${esc(it.label)}</span>`)
        )
        .join("") +
      "</nav>"
    );
  }

  function emptyState(title, text) {
    return `<div class="empty"><h3>${esc(title)}</h3><p>${esc(text)}</p></div>`;
  }

  function eventStats(id) {
    const c = CONTENT[id] || {};
    const ev = EVENTS[id];
    const s = {
      books: ev.books.length,
      booksSummarized: Object.keys(c.summaries || {}).filter((k) => (c.summaries[k] || []).length).length,
      tests: LEVELS.filter((l) => testReady(ev, l.id)).length,
      cards: (c.flashcards || []).reduce((n, d) => n + d.cards.length, 0),
      quizzes: Object.values(c.quizzes || {}).reduce((n, list) => n + list.length, 0),
      guide: !!c.guide,
    };
    s.any = s.booksSummarized + s.tests + s.cards + s.quizzes > 0 || s.guide;
    return s;
  }

  // A practice test opens only once it has exactly as many questions as the real event test.
  function testQuestions(ev, levelId) {
    const c = CONTENT[ev.id];
    return (c && c.tests && c.tests[levelId]) || [];
  }
  function testReady(ev, levelId) {
    return !!ev.hasTest && testQuestions(ev, levelId).length === ev.testQuestions;
  }

  const bookMeta = (b) => [b.author, b.publisher].filter(Boolean).join(" · ");

  function setTitle(t) {
    document.title = t ? `${t} · ${SITE_NAME}` : `${SITE_NAME} · HOSA Prep`;
  }

  // ---------- pages ----------
  let homeState = { q: "", cat: "all" };

  function renderHome() {
    setTitle("");
    app.innerHTML = `
      <section class="hero">
        <h1>Prepare for <span class="grad">every HOSA event</span></h1>
        <p>Chapter summaries, practice tests, and flashcards, organized by competitive event.</p>
        <div class="search">${icon.search}<input id="q" type="search" placeholder="Search ${window.EVENTS.length} events…" value="${esc(homeState.q)}" autocomplete="off" /></div>
      </section>
      <div class="chips" role="tablist">
        <button class="chip" data-cat="all">All events</button>
        ${window.CATEGORIES.map((c) => `<button class="chip" data-cat="${c.id}">${esc(c.name)}</button>`).join("")}
      </div>
      <div id="event-list"></div>`;

    const list = document.getElementById("event-list");
    const input = document.getElementById("q");

    function draw() {
      app.querySelectorAll(".chip").forEach((b) => b.classList.toggle("active", b.dataset.cat === homeState.cat));
      const q = homeState.q.trim().toLowerCase();
      const blocks = window.CATEGORIES.filter((c) => homeState.cat === "all" || homeState.cat === c.id)
        .map((cat) => {
          const evs = window.EVENTS.filter((e) => e.category === cat.id && (!q || e.name.toLowerCase().includes(q)));
          if (!evs.length) return "";
          return `
            <section class="category-block">
              <h2 class="category-title"><span class="dot" style="background:${cat.color}"></span>${esc(cat.name)} <span class="count">${evs.length}</span></h2>
              <div class="grid">
                ${evs
                  .map((e) => {
                    const s = eventStats(e.id);
                    return `<a class="card card-link event-card" href="#/event/${e.id}" style="--cat:${cat.color}">
                      <h3>${esc(e.name)}</h3>
                      <div class="meta"><span>${esc(e.format)}</span>${icon.arrow}</div>
                      ${s.any ? `<span class="ready-dot" title="Study content available">● Study content</span>` : ""}
                    </a>`;
                  })
                  .join("")}
              </div>
            </section>`;
        })
        .join("");
      list.innerHTML = blocks || emptyState("No events found", `Nothing matches "${homeState.q}". Try a different search.`);
    }

    input.addEventListener("input", () => { homeState.q = input.value; draw(); });
    app.querySelectorAll(".chip").forEach((b) => b.addEventListener("click", () => { homeState.cat = b.dataset.cat; draw(); }));
    draw();
  }

  function eventHeader(ev, sub) {
    const cat = CATS[ev.category];
    return `<div class="page-head" style="--cat:${cat.color}">
      <div class="eyebrow">${esc(cat.name)}</div>
      <h1>${esc(sub || ev.name)}</h1>
    </div>`;
  }

  function renderEvent(ev) {
    setTitle(ev.name);
    const s = eventStats(ev.id);
    const cat = CATS[ev.category];
    const guide = CONTENT[ev.id] && CONTENT[ev.id].guide;
    let modes = [
      {
        href: "guide", title: "Study Guide", icon: icon.guide, color: "#8b5cf6",
        text: "How the event runs, exactly how judges score it, and the tips and checklist to prepare.",
        meta: guide ? `${guide.rubrics.length} official rating sheet${guide.rubrics.length === 1 ? "" : "s"} broken down` : "",
        skip: !guide,
      },
      {
        href: "summaries", title: "Chapter Summaries", icon: icon.book, color: "#0d9488",
        text: "Chapter-by-chapter summaries of each official reference for this event.",
        meta: s.books ? `${s.books} official reference${s.books === 1 ? "" : "s"}` : "",
        off: !s.books && "This event has no reference textbooks.",
      },
      {
        href: "quizzes", title: "Chapter Quizzes", icon: icon.quiz, color: "#0ea5e9",
        text: "Short quizzes that each cover three chapters of a book, so you can check yourself as you read.",
        meta: s.quizzes ? `${s.quizzes} quiz${s.quizzes === 1 ? "" : "zes"}` : "Coming soon",
        off: !s.books && "This event has no reference textbooks.",
      },
      {
        href: "tests", title: "Practice Tests", icon: icon.test, color: "#6366f1",
        text: ev.hasTest
          ? `Three ${ev.testQuestions}-question tests, the same length as the real one, from easy to competition level.`
          : "",
        meta: ev.hasTest ? `${s.tests} of 3 ready` : "",
        off: !ev.hasTest && "This event has no written test.",
      },
      {
        href: "flashcards", title: "Flashcards", icon: icon.cards, color: "#f59e0b",
        text: "Key terms and concepts, split into focused sections so you can study in short sets.",
        meta: s.cards ? `${s.cards} cards` : "Coming soon",
      },
    ];
    // Events judged without a written test only show what applies to them.
    modes = modes.filter((m) => !m.skip && (ev.hasTest || m.href === "guide" || (m.href === "summaries" && s.books)));
    const plan = ev.testPlan || [];
    app.innerHTML = `
      ${crumbs([{ label: "Events", href: "#/" }, { label: ev.name }])}
      <div class="page-head" style="--cat:${cat.color}">
        <div class="eyebrow">${esc(cat.name)}</div>
        <h1>${esc(ev.name)}</h1>
        <div class="facts">
          <span class="pill">${esc(ev.format)}</span>
          <span class="pill">${esc(ev.team)}</span>
          <a class="pill pill-link" href="${esc(ev.guideline)}" target="_blank" rel="noopener">Official ${esc(window.GUIDELINE_YEAR)} guidelines ↗</a>
        </div>
        <p>${esc(ev.summary)}</p>
      </div>
      <div class="mode-grid">
        ${modes
          .map((m) => {
            const inner = `
              <div class="mode-icon" style="background:color-mix(in srgb, ${m.color} 14%, transparent);color:${m.color}">${m.icon}</div>
              <h2>${m.title}</h2>
              <p>${m.off || m.text}</p>
              ${m.meta && !m.off ? `<span class="pill" style="align-self:flex-start;margin-top:4px">${m.meta}</span>` : ""}
              ${m.off ? "" : `<span class="go">Open ${icon.arrow}</span>`}`;
            return m.off
              ? `<div class="card mode-card is-off">${inner}</div>`
              : `<a class="card card-link mode-card" href="#/event/${ev.id}/${m.href}">${inner}</a>`;
          })
          .join("")}
      </div>
      <div class="about-grid">
        ${
          plan.length
            ? `<section class="card about">
                <h3>Official test plan</h3>
                <p class="muted">What the ${esc(ev.format.toLowerCase())} covers, from the ${esc(window.GUIDELINE_YEAR)} guidelines.</p>
                <ul class="plan">
                  ${plan
                    .map(
                      (r) => `<li>
                        <div class="plan-row"><span>${esc(r.topic)}</span>${r.pct != null ? `<span class="pct">${r.pct}%</span>` : ""}</div>
                        ${r.pct != null ? `<div class="plan-bar"><div style="width:${Math.min(100, r.pct * 2)}%"></div></div>` : ""}
                        ${r.sub ? `<div class="plan-sub">${r.sub.map(esc).join(" · ")}</div>` : ""}
                      </li>`
                    )
                    .join("")}
                </ul>
              </section>`
            : ""
        }
        ${
          ev.books.length
            ? `<section class="card about">
                <h3>Official references</h3>
                <p class="muted">HOSA lists these as the sources for the test questions.</p>
                <ul class="refs">
                  ${ev.books
                    .map((b) => `<li><strong>${esc(b.title)}</strong><span>${esc(bookMeta(b))}${b.note ? ` · <em>${esc(b.note)}</em>` : ""}</span></li>`)
                    .join("")}
                </ul>
              </section>`
            : ""
        }
      </div>`;
  }

  function renderBooks(ev) {
    setTitle(`${ev.name} Summaries`);
    const books = ev.books;
    const sums = (CONTENT[ev.id] && CONTENT[ev.id].summaries) || {};
    const cat = CATS[ev.category];
    app.innerHTML = `
      ${crumbs([{ label: "Events", href: "#/" }, { label: ev.name, href: `#/event/${ev.id}` }, { label: "Chapter Summaries" }])}
      ${eventHeader(ev, "Chapter Summaries")}
      <p style="color:var(--text-2);margin:-16px 0 24px">These are the official references from the ${esc(window.GUIDELINE_YEAR)} guidelines. Pick one to read its chapter summaries.</p>
      ${
        books.length
          ? `<div class="list">${books
              .map((b, i) => {
                const n = (sums[i] || []).length;
                return `<a class="card card-link book-card" style="--cat:${cat.color}" href="#/event/${ev.id}/summaries/${i}">
                  <div class="book-cover">${i + 1}</div>
                  <div style="flex:1;min-width:0"><h3>${esc(b.title)}</h3><p>${esc(bookMeta(b))}${b.note ? ` · ${esc(b.note)}` : ""}</p></div>
                  <span class="pill">${n ? `${n} chapter${n === 1 ? "" : "s"}` : "Coming soon"}</span>
                </a>`;
              })
              .join("")}</div>`
          : emptyState("No reference textbooks", "This event doesn't use reference textbooks.")
      }`;
  }

  function renderChapters(ev, bookIdx) {
    const meta = ev.books[bookIdx];
    if (!meta) return renderNotFound();
    const book = { ...meta, chapters: ((CONTENT[ev.id] && CONTENT[ev.id].summaries) || {})[bookIdx] || [] };
    setTitle(`${book.title} · ${ev.name}`);
    if (!book.chapters.length) {
      app.innerHTML = `
        ${crumbs([
          { label: "Events", href: "#/" },
          { label: ev.name, href: `#/event/${ev.id}` },
          { label: "Chapter Summaries", href: `#/event/${ev.id}/summaries` },
          { label: book.title },
        ])}
        ${eventHeader(ev, book.title)}
        ${emptyState("Summaries coming soon", `Chapter summaries for ${book.title} haven't been added yet.`)}`;
      return;
    }
    app.innerHTML = `
      ${crumbs([
        { label: "Events", href: "#/" },
        { label: ev.name, href: `#/event/${ev.id}` },
        { label: "Chapter Summaries", href: `#/event/${ev.id}/summaries` },
        { label: book.title },
      ])}
      ${eventHeader(ev, book.title)}
      <div class="reader">
        <aside class="card toc">
          <h4>Chapters</h4>
          ${book.chapters.map((c, i) => `<a href="#ch-${i}" data-ch="${i}"><span class="num">${c.number || i + 1}</span><span>${esc(c.title)}</span></a>`).join("")}
        </aside>
        <div>
          ${book.chapters
            .map(
              (c, i) => `<article class="card chapter" id="ch-${i}">
                <div class="num-label">Chapter ${c.number || i + 1}</div>
                <h2>${esc(c.title)}</h2>
                ${(c.summary || []).map((p) => `<p>${esc(p)}</p>`).join("")}
                ${
                  c.keyPoints && c.keyPoints.length
                    ? `<div class="keypoints"><h4>Key points</h4><ul>${c.keyPoints.map((k) => `<li>${esc(k)}</li>`).join("")}</ul></div>`
                    : ""
                }
              </article>`
            )
            .join("")}
        </div>
      </div>`;

    // TOC links scroll without changing the route
    const links = app.querySelectorAll(".toc a");
    links.forEach((a) =>
      a.addEventListener("click", (e) => {
        e.preventDefault();
        document.getElementById("ch-" + a.dataset.ch).scrollIntoView({ behavior: "smooth" });
      })
    );
    const obs = new IntersectionObserver(
      (entries) => {
        entries.forEach((en) => {
          if (en.isIntersecting) {
            const i = en.target.id.slice(3);
            links.forEach((l) => l.classList.toggle("active", l.dataset.ch === i));
          }
        });
      },
      { rootMargin: "-90px 0px -60% 0px" }
    );
    app.querySelectorAll(".chapter").forEach((el) => obs.observe(el));
    cleanup = () => obs.disconnect();
  }

  function renderTests(ev) {
    setTitle(`${ev.name} Practice Tests`);
    const tests = (CONTENT[ev.id] && CONTENT[ev.id].tests) || {};
    const best = store.get(`best:${ev.id}`, {});
    if (!ev.hasTest) {
      app.innerHTML = `
        ${crumbs([{ label: "Events", href: "#/" }, { label: ev.name, href: `#/event/${ev.id}` }, { label: "Practice Tests" }])}
        ${eventHeader(ev, "Practice Tests")}
        ${emptyState("No written test", `${ev.name} is judged on a ${ev.format.toLowerCase()}, not a written test.`)}`;
      return;
    }
    app.innerHTML = `
      ${crumbs([{ label: "Events", href: "#/" }, { label: ev.name, href: `#/event/${ev.id}` }, { label: "Practice Tests" }])}
      ${eventHeader(ev, "Practice Tests")}
      <p style="color:var(--text-2);margin:-16px 0 24px">Each practice test matches the real Round One test: ${ev.testQuestions} multiple-choice questions, ${ev.testMinutes} minutes.</p>
      <div class="mode-grid">
        ${LEVELS.map((l, i) => {
          const ready = testReady(ev, l.id);
          const inner = `
            <div class="level-badge" style="--lvl:${l.color}">${[1, 2, 3].map((n) => `<span class="${n <= l.bars ? "on" : ""}"></span>`).join("")}</div>
            <h2>Test ${i + 1}: ${l.name}</h2>
            <p>${l.blurb}</p>
            <div class="meta">${ready ? `${ev.testQuestions} questions · ${ev.testMinutes} min` : "Coming soon"}${ready && best[l.id] != null ? ` · Best score ${best[l.id]}%` : ""}</div>`;
          return ready
            ? `<a class="card card-link level-card" href="#/event/${ev.id}/tests/${l.id}">${inner}</a>`
            : `<div class="card level-card" style="opacity:.6">${inner}</div>`;
        }).join("")}
      </div>`;
  }

  function renderQuiz(ev, levelId) {
    const level = LEVELS.find((l) => l.id === levelId);
    if (!level || !testReady(ev, levelId)) return renderNotFound();
    setTitle(`${level.name} Test · ${ev.name}`);
    runQuiz({
      qs: testQuestions(ev, levelId),
      head: crumbs([
        { label: "Events", href: "#/" },
        { label: ev.name, href: `#/event/${ev.id}` },
        { label: "Practice Tests", href: `#/event/${ev.id}/tests` },
        { label: level.name },
      ]),
      label: `${level.name} · ${ev.name}`,
      resultText: (c, n) => `You got ${c} of ${n} questions right on the ${level.name.toLowerCase()} test.`,
      bestKey: `best:${ev.id}`, bestField: levelId,
      retryLabel: "Retake test", backHref: `#/event/${ev.id}/tests`, backLabel: "All tests",
    });
  }

  // ---------- chapter quizzes (one per 3 chapters of a book) ----------
  const chapterRange = (chs) => (chs.length > 1 ? `Chapters ${chs[0]}–${chs[chs.length - 1]}` : `Chapter ${chs[0]}`);
  const bookQuizzes = (ev, bookIdx) => ((CONTENT[ev.id] && CONTENT[ev.id].quizzes) || {})[bookIdx] || [];

  function renderQuizBooks(ev) {
    setTitle(`${ev.name} Chapter Quizzes`);
    const cat = CATS[ev.category];
    app.innerHTML = `
      ${crumbs([{ label: "Events", href: "#/" }, { label: ev.name, href: `#/event/${ev.id}` }, { label: "Chapter Quizzes" }])}
      ${eventHeader(ev, "Chapter Quizzes")}
      <p style="color:var(--text-2);margin:-16px 0 24px">Short quizzes that each cover three chapters of a book. Pick a book.</p>
      ${
        ev.books.length
          ? `<div class="list">${ev.books
              .map((b, i) => {
                const n = bookQuizzes(ev, i).length;
                return `<a class="card card-link book-card" style="--cat:${cat.color}" href="#/event/${ev.id}/quizzes/${i}">
                  <div class="book-cover">${i + 1}</div>
                  <div style="flex:1;min-width:0"><h3>${esc(b.title)}</h3><p>${esc(bookMeta(b))}${b.note ? ` · ${esc(b.note)}` : ""}</p></div>
                  <span class="pill">${n ? `${n} quiz${n === 1 ? "" : "zes"}` : "Coming soon"}</span>
                </a>`;
              })
              .join("")}</div>`
          : emptyState("No reference textbooks", "This event doesn't use reference textbooks, so there are no chapter quizzes.")
      }`;
  }

  function renderQuizList(ev, bookIdx) {
    const book = ev.books[bookIdx];
    if (!book) return renderNotFound();
    setTitle(`${book.title} Quizzes · ${ev.name}`);
    const qz = bookQuizzes(ev, bookIdx);
    const best = store.get(`qbest:${ev.id}:${bookIdx}`, {});
    app.innerHTML = `
      ${crumbs([
        { label: "Events", href: "#/" },
        { label: ev.name, href: `#/event/${ev.id}` },
        { label: "Chapter Quizzes", href: `#/event/${ev.id}/quizzes` },
        { label: book.title },
      ])}
      ${eventHeader(ev, book.title)}
      ${
        qz.length
          ? `<div class="grid">
              ${qz
                .map(
                  (z, i) => `<a class="card card-link deck-card" href="#/event/${ev.id}/quizzes/${bookIdx}/${i}">
                    <span class="pill" style="align-self:flex-start;margin-bottom:6px">Quiz ${i + 1}</span>
                    <h3>${chapterRange(z.chapters)}</h3>
                    <p>${z.questions.length} questions</p>
                    <div class="stack"><span>${best[i] != null ? `Best score ${best[i]}%` : "Not taken yet"}</span></div>
                  </a>`
                )
                .join("")}
            </div>
            <p class="muted" style="margin-top:18px">More quizzes for this book are coming soon.</p>`
          : emptyState("Quizzes coming soon", `Chapter quizzes for ${book.title} haven't been added yet.`)
      }`;
  }

  function renderChapterQuiz(ev, bookIdx, quizIdx) {
    const book = ev.books[bookIdx];
    const z = book && bookQuizzes(ev, bookIdx)[quizIdx];
    if (!z || !z.questions.length) return renderNotFound();
    const range = chapterRange(z.chapters);
    setTitle(`${range} Quiz · ${book.title}`);
    runQuiz({
      qs: z.questions,
      head: crumbs([
        { label: "Events", href: "#/" },
        { label: ev.name, href: `#/event/${ev.id}` },
        { label: "Chapter Quizzes", href: `#/event/${ev.id}/quizzes` },
        { label: book.title, href: `#/event/${ev.id}/quizzes/${bookIdx}` },
        { label: range },
      ]),
      label: `${range} · ${book.title}`,
      resultText: (c, n) => `You got ${c} of ${n} questions right on the ${range.toLowerCase()} quiz.`,
      bestKey: `qbest:${ev.id}:${bookIdx}`, bestField: quizIdx,
      retryLabel: "Retake quiz", backHref: `#/event/${ev.id}/quizzes/${bookIdx}`, backLabel: "All quizzes",
    });
  }

  // Shared question-by-question runner for practice tests and chapter quizzes.
  function runQuiz(o) {
    const qs = o.qs;
    let idx = 0;
    const answers = new Array(qs.length).fill(null);
    const head = o.head;

    function drawQuestion() {
      const q = qs[idx];
      const chosen = answers[idx];
      const done = chosen !== null;
      app.innerHTML = `${head}
        <div class="quiz">
          <div class="progress"><div style="width:${((idx + (done ? 1 : 0)) / qs.length) * 100}%"></div></div>
          <div class="quiz-meta"><span>Question ${idx + 1} of ${qs.length}</span><span>${esc(o.label)}</span></div>
          <div class="card question">
            <h2>${esc(q.q)}</h2>
            <div class="options">
              ${q.options
                .map((o, i) => {
                  let cls = "";
                  if (done && i === q.answer) cls = "correct";
                  else if (done && i === chosen) cls = "wrong";
                  return `<button class="option ${cls}" data-i="${i}" ${done ? "disabled" : ""}><span class="key">${"ABCD"[i]}</span><span>${esc(o)}</span></button>`;
                })
                .join("")}
            </div>
            ${
              done
                ? `<div class="explanation"><strong>${chosen === q.answer ? "Correct." : "Not quite."}</strong> ${esc(q.explanation || "")}</div>`
                : ""
            }
          </div>
          <div class="quiz-actions">
            ${done ? `<button class="btn btn-primary" id="next">${idx === qs.length - 1 ? "See results" : "Next question"} ${icon.arrow}</button>` : ""}
          </div>
          <p class="kbd-hint">Press <kbd>A</kbd>–<kbd>D</kbd> to answer, <kbd>Enter</kbd> to continue</p>
        </div>`;
      app.querySelectorAll(".option").forEach((b) => b.addEventListener("click", () => choose(+b.dataset.i)));
      const next = document.getElementById("next");
      if (next) next.addEventListener("click", advance);
    }

    function choose(i) {
      if (answers[idx] !== null || i >= qs[idx].options.length) return;
      answers[idx] = i;
      drawQuestion();
      const n = document.getElementById("next");
      if (n) n.focus({ preventScroll: true });
    }

    function advance() {
      if (answers[idx] === null) return;
      if (idx < qs.length - 1) { idx++; drawQuestion(); window.scrollTo({ top: 0 }); }
      else drawResult();
    }

    function drawResult() {
      const correct = answers.filter((a, i) => a === qs[i].answer).length;
      const pct = Math.round((correct / qs.length) * 100);
      const best = store.get(o.bestKey, {});
      if (best[o.bestField] == null || pct > best[o.bestField]) { best[o.bestField] = pct; store.set(o.bestKey, best); }
      const r = 60, circ = 2 * Math.PI * r;
      const color = pct >= 80 ? "var(--good)" : pct >= 60 ? "#f59e0b" : "var(--bad)";
      const msg = pct >= 90 ? "Excellent work!" : pct >= 70 ? "Nice job!" : pct >= 50 ? "Getting there." : "Keep practicing.";
      app.innerHTML = `${head}
        <div class="quiz">
          <div class="card result">
            <div class="score-ring">
              <svg width="140" height="140"><circle cx="70" cy="70" r="${r}" fill="none" stroke="var(--surface-2)" stroke-width="12"/>
              <circle cx="70" cy="70" r="${r}" fill="none" stroke="${color}" stroke-width="12" stroke-linecap="round" stroke-dasharray="${circ}" stroke-dashoffset="${circ * (1 - pct / 100)}"/></svg>
              <div class="val">${pct}%</div>
            </div>
            <h2>${msg}</h2>
            <p>${esc(o.resultText(correct, qs.length))}</p>
            <div class="actions">
              <button class="btn btn-primary" id="retry">${esc(o.retryLabel)}</button>
              <a class="btn" href="${o.backHref}">${esc(o.backLabel)}</a>
            </div>
          </div>
          <h3 style="margin:32px 0 4px">Review answers</h3>
          <div class="review">
            ${qs
              .map((q, i) => {
                const ok = answers[i] === q.answer;
                return `<div class="card review-item">
                  <div class="q">${i + 1}. ${esc(q.q)}</div>
                  <div class="a">${
                    ok
                      ? `<span class="ok">✓ ${esc(q.options[q.answer])}</span>`
                      : `<span class="no">✗ ${esc(q.options[answers[i]])}</span> · Correct: <span class="ok">${esc(q.options[q.answer])}</span>`
                  }</div>
                </div>`;
              })
              .join("")}
          </div>
        </div>`;
      document.getElementById("retry").addEventListener("click", () => {
        idx = 0; answers.fill(null); drawQuestion();
      });
      window.scrollTo({ top: 0 });
    }

    const onKey = (e) => {
      if (e.target.tagName === "INPUT" || e.metaKey || e.ctrlKey || e.altKey) return;
      const k = e.key.toLowerCase();
      if ("abcd".includes(k) && k.length === 1 && app.querySelector(".option")) choose("abcd".indexOf(k));
      else if (e.key === "Enter" && answers[idx] !== null && app.querySelector("#next") && document.activeElement !== app.querySelector("#next")) advance();
    };
    document.addEventListener("keydown", onKey);
    cleanup = () => document.removeEventListener("keydown", onKey);
    drawQuestion();
  }

  function renderDecks(ev) {
    setTitle(`${ev.name} Flashcards`);
    const decks = (CONTENT[ev.id] && CONTENT[ev.id].flashcards) || [];
    const known = store.get(`known:${ev.id}`, {});
    const total = decks.reduce((n, d) => n + d.cards.length, 0);
    app.innerHTML = `
      ${crumbs([{ label: "Events", href: "#/" }, { label: ev.name, href: `#/event/${ev.id}` }, { label: "Flashcards" }])}
      ${eventHeader(ev, "Flashcards")}
      ${
        decks.length
          ? `<p style="color:var(--text-2);margin:-16px 0 24px">${total} cards across ${decks.length} sections. Pick a section to study.</p>
            <div class="grid">
              ${decks
                .map((d, i) => {
                  const k = (known[i] || []).filter((x) => x < d.cards.length).length;
                  return `<a class="card card-link deck-card" href="#/event/${ev.id}/flashcards/${i}">
                    <span class="pill" style="align-self:flex-start;margin-bottom:6px">Section ${i + 1}</span>
                    <h3>${esc(d.section)}</h3>
                    <p>${esc(d.description || "")}</p>
                    <div class="stack"><span>${d.cards.length} cards · ${k} known</span><div class="mini-bar"><div style="width:${(k / d.cards.length) * 100}%"></div></div></div>
                  </a>`;
                })
                .join("")}
            </div>`
          : emptyState("Flashcards coming soon", "Flashcard sections for this event haven't been added yet.")
      }`;
  }

  function renderStudy(ev, deckIdx) {
    const decks = (CONTENT[ev.id] && CONTENT[ev.id].flashcards) || [];
    const deck = decks[deckIdx];
    if (!deck) return renderNotFound();
    setTitle(`${deck.section} · ${ev.name}`);

    const knownAll = store.get(`known:${ev.id}`, {});
    const known = new Set(knownAll[deckIdx] || []);
    let order = deck.cards.map((_, i) => i);
    let pos = 0;
    let flipped = false;
    let onlyUnknown = false;

    function saveKnown() {
      knownAll[deckIdx] = [...known];
      store.set(`known:${ev.id}`, knownAll);
    }
    function visible() {
      return onlyUnknown ? order.filter((i) => !known.has(i)) : order;
    }

    function draw() {
      const list = visible();
      if (pos >= list.length) pos = Math.max(0, list.length - 1);
      const base = `
        ${crumbs([
          { label: "Events", href: "#/" },
          { label: ev.name, href: `#/event/${ev.id}` },
          { label: "Flashcards", href: `#/event/${ev.id}/flashcards` },
          { label: deck.section },
        ])}
        ${eventHeader(ev, deck.section)}`;

      const toolbar = `<div class="study-toolbar">
          <label class="toggle"><input type="checkbox" id="only" ${onlyUnknown ? "checked" : ""}/> Only show cards I'm still learning</label>
          <div style="display:flex;gap:8px">
            <button class="btn" id="shuffle">${icon.shuffle} Shuffle</button>
            <button class="btn" id="reset">Reset progress</button>
          </div>
        </div>`;

      if (!list.length) {
        app.innerHTML = `${base}<div class="study">${toolbar}${emptyState("You know every card in this section 🎉", "Turn off the filter to review them all again, or reset your progress.")}</div>`;
        bindToolbar();
        return;
      }
      const card = deck.cards[list[pos]];
      const isKnown = known.has(list[pos]);
      app.innerHTML = `${base}
        <div class="study">
          ${toolbar}
          <div class="progress"><div style="width:${(known.size / deck.cards.length) * 100}%;background:var(--good)"></div></div>
          <div class="quiz-meta"><span>${known.size} of ${deck.cards.length} known</span>${isKnown ? '<span style="color:var(--good);font-weight:600">✓ Known</span>' : "<span></span>"}</div>
          <div class="flip ${flipped ? "flipped" : ""}" id="flip" role="button" tabindex="0" aria-label="Flip card">
            <div class="flip-inner">
              <div class="face front"><span class="label">Term</span><div class="content">${esc(card.front)}</div><span class="hint">Click or press Space to flip</span></div>
              <div class="face back"><span class="label">Definition</span><div class="content">${esc(card.back)}</div></div>
            </div>
          </div>
          <div class="study-controls">
            <button class="btn" id="prev" ${pos === 0 ? "disabled" : ""}>${icon.left} Prev</button>
            <span class="counter">${pos + 1} / ${list.length}</span>
            <button class="btn" id="next" ${pos === list.length - 1 ? "disabled" : ""}>Next ${icon.right}</button>
          </div>
          <div class="know-row">
            <button class="btn btn-bad" id="learning">Still learning</button>
            <button class="btn btn-good" id="know">I know this</button>
          </div>
          <p class="kbd-hint"><kbd>Space</kbd> flip · <kbd>←</kbd> <kbd>→</kbd> navigate · <kbd>1</kbd> still learning · <kbd>2</kbd> know it</p>
        </div>`;

      document.getElementById("flip").addEventListener("click", flip);
      document.getElementById("prev").addEventListener("click", () => move(-1));
      document.getElementById("next").addEventListener("click", () => move(1));
      document.getElementById("know").addEventListener("click", () => mark(true));
      document.getElementById("learning").addEventListener("click", () => mark(false));
      bindToolbar();
    }

    function bindToolbar() {
      document.getElementById("only").addEventListener("change", (e) => { onlyUnknown = e.target.checked; pos = 0; flipped = false; draw(); });
      document.getElementById("shuffle").addEventListener("click", () => {
        for (let i = order.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [order[i], order[j]] = [order[j], order[i]]; }
        pos = 0; flipped = false; draw();
      });
      document.getElementById("reset").addEventListener("click", () => { known.clear(); saveKnown(); pos = 0; flipped = false; draw(); });
    }

    function flip() {
      flipped = !flipped;
      const el = document.getElementById("flip");
      if (el) el.classList.toggle("flipped", flipped);
    }
    function move(d) {
      const list = visible();
      const n = pos + d;
      if (n < 0 || n >= list.length) return;
      pos = n; flipped = false; draw();
    }
    function mark(isKnown) {
      const list = visible();
      if (!list.length) return;
      const id = list[pos];
      if (isKnown) known.add(id); else known.delete(id);
      saveKnown();
      flipped = false;
      // In filtered mode a newly-known card drops out of the list, so the same pos now shows the next card.
      if (!(onlyUnknown && isKnown) && pos < list.length - 1) pos++;
      draw();
    }

    const onKey = (e) => {
      if (e.target.tagName === "INPUT" || e.metaKey || e.ctrlKey || e.altKey) return;
      if (e.key === " " || e.key === "Enter") { e.preventDefault(); flip(); }
      else if (e.key === "ArrowLeft") move(-1);
      else if (e.key === "ArrowRight") move(1);
      else if (e.key === "1") mark(false);
      else if (e.key === "2") mark(true);
    };
    document.addEventListener("keydown", onKey);
    cleanup = () => document.removeEventListener("keydown", onKey);
    draw();
  }

  function renderGuide(ev) {
    const g = CONTENT[ev.id] && CONTENT[ev.id].guide;
    setTitle(`${ev.name} Study Guide`);
    const head = `${crumbs([{ label: "Events", href: "#/" }, { label: ev.name, href: `#/event/${ev.id}` }, { label: "Study Guide" }])}
      ${eventHeader(ev, "Study Guide")}`;
    if (!g) {
      app.innerHTML = head + emptyState("Coming soon", `A study guide for ${ev.name} hasn't been written yet.`);
      return;
    }
    const key = `check:${ev.id}`;
    const done = store.get(key, {});
    const list = (items, cls) => `<ul class="${cls}">${items.map((t) => `<li>${esc(t)}</li>`).join("")}</ul>`;
    const rubric = (r) => {
      const max = Math.max(...r.sections.flatMap((s) => s.items.map((i) => i.points)));
      return `<section class="card guide-block">
        <div class="rubric-head"><h3>${esc(r.title)}</h3><span class="pill">${esc(r.pill || `${r.total} points`)}</span></div>
        ${r.note ? `<p class="muted">${esc(r.note)}</p>` : ""}
        ${r.sections.map((s) => {
          const sub = s.items.reduce((n, i) => n + i.points, 0);
          return `<div class="rubric-sec">
            <div class="rubric-sec-head"><span>${esc(s.name)}</span>${r.pill ? "" : `<span>${sub} pts</span>`}</div>
            <ul class="rubric-items">${s.items.map((i) => `<li>
              <span class="crit">${esc(i.criterion)}</span>
              <span class="bar"><span style="width:${(i.points / max) * 100}%"></span></span>
              <span class="pts">${i.points}</span></li>`).join("")}</ul>
          </div>`;
        }).join("")}
      </section>`;
    };
    app.innerHTML = `${head}
      <div class="facts" style="margin:-12px 0 18px">
        ${g.facts.map((f) => `<span class="pill"><strong>${esc(f.label)}:</strong>&nbsp;${esc(f.value)}</span>`).join("")}
        <a class="pill pill-link" href="${esc(ev.guideline)}" target="_blank" rel="noopener">Official guidelines ↗</a>
      </div>
      <p class="guide-lede">${esc(g.overview)}</p>
      <nav class="guide-toc">
        <a href="#g-rounds">How it runs</a><a href="#g-score">How it's scored</a><a href="#g-tips">Tips</a><a href="#g-mistakes">Mistakes to avoid</a><a href="#g-check">Checklist</a>
      </nav>
      <h2 class="guide-h" id="g-rounds">How the event runs</h2>
      <div class="rounds">
        ${g.rounds.map((r, i) => `<section class="card guide-block round">
          <div class="round-num">${i + 1}</div>
          <div><h3>${esc(r.title)}</h3>${list(r.steps, "steps")}</div>
        </section>`).join("")}
      </div>
      <h2 class="guide-h" id="g-score">How judges score it</h2>
      <p class="muted" style="margin-top:-6px">Maximum points per item, from the official rating sheets. Bigger bars are where the points are.</p>
      <div class="rubrics">${g.rubrics.map(rubric).join("")}</div>
      <div class="about-grid">
        <section class="card guide-block" id="g-tips"><h3>Tips to score high</h3>${list(g.tips, "tips")}</section>
        <section class="card guide-block" id="g-mistakes"><h3>Common mistakes</h3>${list(g.mistakes, "mistakes")}</section>
      </div>
      <section class="card guide-block" id="g-check" style="margin-top:18px">
        <div class="rubric-head"><h3>Prep checklist</h3><span class="pill" id="check-count"></span></div>
        <ul class="checklist">${g.checklist.map((t, i) => `<li><label><input type="checkbox" data-i="${i}" ${done[i] ? "checked" : ""}/> <span>${esc(t)}</span></label></li>`).join("")}</ul>
      </section>`;
    const count = () => {
      const n = app.querySelectorAll(".checklist input:checked").length;
      document.getElementById("check-count").textContent = `${n} of ${g.checklist.length} done`;
    };
    app.querySelectorAll(".checklist input").forEach((cb) =>
      cb.addEventListener("change", () => {
        const d = store.get(key, {});
        d[cb.dataset.i] = cb.checked;
        store.set(key, d);
        count();
      })
    );
    app.querySelectorAll(".guide-toc a").forEach((a) =>
      a.addEventListener("click", (e) => {
        e.preventDefault();
        document.querySelector(a.getAttribute("href")).scrollIntoView({ behavior: "smooth", block: "start" });
      })
    );
    count();
  }

  function renderNotFound() {
    setTitle("Not found");
    app.innerHTML = `${crumbs([{ label: "Events", href: "#/" }])}${emptyState("Page not found", "That page doesn't exist. Head back to the event list.")}`;
  }

  // ---------- router ----------
  let cleanup = null;

  function route() {
    if (cleanup) { cleanup(); cleanup = null; }
    const parts = location.hash.replace(/^#\/?/, "").split("/").filter(Boolean);
    if (!parts.length) renderHome();
    else if (parts[0] === "event" && EVENTS[parts[1]]) {
      const ev = EVENTS[parts[1]];
      const [, , section, sub] = parts;
      if (!section) renderEvent(ev);
      else if (section === "summaries") sub == null ? renderBooks(ev) : renderChapters(ev, +sub);
      else if (section === "tests") sub == null ? renderTests(ev) : renderQuiz(ev, sub);
      else if (section === "quizzes") {
        const n = parts[4];
        if (sub == null) renderQuizBooks(ev);
        else if (n == null) renderQuizList(ev, +sub);
        else renderChapterQuiz(ev, +sub, +n);
      }
      else if (section === "flashcards") sub == null ? renderDecks(ev) : renderStudy(ev, +sub);
      else if (section === "guide") renderGuide(ev);
      else renderNotFound();
    } else renderNotFound();
    window.scrollTo({ top: 0 });
    app.focus({ preventScroll: true });
  }

  // ---------- theme ----------
  const root = document.documentElement;
  const savedTheme = store.get("theme", null);
  const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  root.dataset.theme = savedTheme || (prefersDark ? "dark" : "light");
  document.getElementById("theme-toggle").addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    store.set("theme", root.dataset.theme);
  });

  document.querySelectorAll("[data-site-name]").forEach((el) => (el.textContent = SITE_NAME));
  window.addEventListener("hashchange", route);
  route();
})();
