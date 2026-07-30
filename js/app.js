/* OffCam — App-Logik (Demo, kein Backend: alles bleibt im Browser) */

(function () {
  "use strict";

  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));

  const gate = $("#gate");
  const landing = $("#landing");
  const app = $("#app");
  const deckEl = $("#deck");
  const deckEmpty = $("#deck-empty");
  const deckActions = $("#deck-actions");
  const matchModal = $("#match-modal");
  const toastEl = $("#toast");

  const state = {
    filter: "alle",
    deck: [],
    matches: [],        // { creator, messages: [{who, text, time}], unread, replyIdx }
    activeChat: null,
    pendingMatch: null
  };

  /* ── Helpers ─────────────────────────────────────────────── */

  const now = () =>
    new Date().toLocaleTimeString("de-DE", { hour: "2-digit", minute: "2-digit" });

  let toastTimer = null;
  function toast(msg) {
    toastEl.textContent = msg;
    toastEl.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { toastEl.hidden = true; }, 2600);
  }

  function avatarHTML(c, cls) {
    const initial = c.initial || c.name[0];
    return `<span class="avatar ${cls || ""}" style="--ha:${c.ha};--hb:${c.hb}" aria-hidden="true">${initial}</span>`;
  }

  const checkSVG =
    '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>';

  /* ── Age Gate ────────────────────────────────────────────── */

  function enterSite() {
    gate.hidden = true;
    landing.hidden = false;
  }

  let ageOk = false;
  try { ageOk = localStorage.getItem("offcam_age18") === "1"; } catch (e) { /* privat-modus */ }

  if (ageOk) {
    enterSite();
  } else {
    gate.hidden = false;
  }

  $("#gate-yes").addEventListener("click", () => {
    try { localStorage.setItem("offcam_age18", "1"); } catch (e) { /* egal */ }
    enterSite();
  });

  $("#gate-no").addEventListener("click", () => {
    $$(".gate-inner", gate)[0].hidden = true;
    $("#gate-denied").hidden = false;
  });

  /* ── Landing ⇄ App ───────────────────────────────────────── */

  $$("[data-open-app]").forEach((btn) =>
    btn.addEventListener("click", () => {
      landing.hidden = true;
      app.hidden = false;
      if (!state.deck.length && !dealtOnce) deal();
    })
  );

  $("#app-exit").addEventListener("click", () => {
    app.hidden = true;
    landing.hidden = false;
  });

  /* ── Toast-Buttons (Platzhalter-Links etc.) ──────────────── */

  $$("[data-toast]").forEach((el) =>
    el.addEventListener("click", (e) => {
      e.preventDefault();
      toast(el.dataset.toast);
    })
  );

  /* ── Tabs ────────────────────────────────────────────────── */

  const views = {
    discover: $("#view-discover"),
    chats: $("#view-chats"),
    profile: $("#view-profile")
  };

  function showView(name) {
    Object.entries(views).forEach(([key, el]) => { el.hidden = key !== name; });
    $$(".tab").forEach((t) => {
      const active = t.dataset.view === name;
      t.classList.toggle("is-active", active);
      if (active) t.setAttribute("aria-current", "page");
      else t.removeAttribute("aria-current");
    });
    if (name === "chats") renderChatList();
  }

  $$(".tab").forEach((t) =>
    t.addEventListener("click", () => showView(t.dataset.view))
  );

  /* ── Deck ────────────────────────────────────────────────── */

  let dealtOnce = false;

  function matchedIds() {
    return new Set(state.matches.map((m) => m.creator.id));
  }

  function deal() {
    dealtOnce = true;
    const taken = matchedIds();
    state.deck = CREATORS.filter((c) => {
      if (taken.has(c.id)) return false;
      if (state.filter === "alle") return true;
      return c.goal === state.filter || c.goal === "both";
    });
    renderDeck();
  }

  function cardHTML(c) {
    return `
      <div class="card-art" aria-hidden="true">
        <span class="blob blob-a"></span>
        <span class="blob blob-b"></span>
        <span class="card-initials">${c.name[0]}</span>
        <span class="card-ring"><span class="card-emoji">${c.emoji}</span></span>
      </div>
      <div class="card-top" aria-hidden="true">
        ${c.likesYou ? '<span class="pill"><span class="rec-dot rec-dot-live"></span>Online</span>' : "<span></span>"}
        <span class="pill">${c.km} km</span>
      </div>
      <span class="stamp stamp-like">LIKE</span>
      <span class="stamp stamp-nope">NOPE</span>
      <div class="card-info">
        <div class="card-name">${c.name}, ${c.age} <span class="verified" title="Verifizierter Creator">${checkSVG}</span></div>
        <div class="card-meta mono">${c.city.toUpperCase()} · ${c.followers.toUpperCase()} FOLLOWER</div>
        <p class="card-bio">${c.bio}</p>
        <div class="card-tags">
          <span class="tag tag-goal">${c.goalLabel}</span>
          ${c.tags.map((t) => `<span class="tag">${t}</span>`).join("")}
        </div>
      </div>`;
  }

  const STACK = [
    { y: 0, s: 1 },
    { y: 12, s: 0.955 },
    { y: 24, s: 0.91 }
  ];

  function renderDeck() {
    deckEl.innerHTML = "";
    const visible = state.deck.slice(0, 3);
    const empty = visible.length === 0;
    deckEmpty.hidden = !empty;
    deckActions.style.visibility = empty ? "hidden" : "visible";
    if (empty) return;

    // Unterste Karte zuerst ins DOM, oberste zuletzt (liegt damit oben)
    for (let i = visible.length - 1; i >= 0; i--) {
      const c = visible[i];
      const card = document.createElement("article");
      card.className = "card";
      card.style.setProperty("--ha", c.ha);
      card.style.setProperty("--hb", c.hb);
      card.dataset.id = c.id;
      card.innerHTML = cardHTML(c);
      const pos = STACK[i];
      if (i > 0) card.style.transform = `translateY(${pos.y}px) scale(${pos.s})`;
      else {
        card.classList.add("is-top", "deal-in");
        card.addEventListener("animationend", () => card.classList.remove("deal-in"), { once: true });
      }
      deckEl.appendChild(card);
    }
    attachDrag(deckEl.lastElementChild);
  }

  /* Drag / Swipe */

  function attachDrag(card) {
    if (!card) return;
    let start = null;

    const stampLike = $(".stamp-like", card);
    const stampNope = $(".stamp-nope", card);

    card.addEventListener("pointerdown", (e) => {
      if (card.classList.contains("fly-out")) return;
      start = { x: e.clientX, y: e.clientY };
      card.classList.remove("deal-in");
      card.classList.add("is-dragging");
      card.setPointerCapture(e.pointerId);
    });

    card.addEventListener("pointermove", (e) => {
      if (!start) return;
      const dx = e.clientX - start.x;
      const dy = e.clientY - start.y;
      card.style.transform = `translate(${dx}px, ${dy * 0.35}px) rotate(${dx * 0.055}deg)`;
      stampLike.style.opacity = Math.min(1, Math.max(0, dx / 80));
      stampNope.style.opacity = Math.min(1, Math.max(0, -dx / 80));
    });

    const release = (e) => {
      if (!start) return;
      const dx = e.clientX - start.x;
      start = null;
      card.classList.remove("is-dragging");
      if (dx > 90) swipe("like");
      else if (dx < -90) swipe("nope");
      else {
        card.style.transform = "";
        stampLike.style.opacity = 0;
        stampNope.style.opacity = 0;
      }
    };

    card.addEventListener("pointerup", release);
    card.addEventListener("pointercancel", release);
  }

  let swiping = false;

  function swipe(action) {
    if (swiping || !state.deck.length) return;
    const card = deckEl.lastElementChild;
    const creator = state.deck[0];
    if (!card) return;
    swiping = true;

    card.classList.remove("is-dragging");
    card.classList.add("fly-out");

    if (action === "like") {
      $(".stamp-like", card).style.opacity = 1;
      card.style.transform = "translate(120vw, -6vh) rotate(22deg)";
    } else if (action === "nope") {
      $(".stamp-nope", card).style.opacity = 1;
      card.style.transform = "translate(-120vw, -6vh) rotate(-22deg)";
    } else {
      card.style.transform = "translateY(-130%) rotate(-4deg)";
      card.style.opacity = "0";
    }

    setTimeout(() => {
      state.deck.shift();
      renderDeck();
      swiping = false;

      if (action === "like" && creator.likesYou) openMatch(creator);
      if (action === "collab") {
        toast(`⚡ Collab-Anfrage an ${creator.name} geschickt (Demo)`);
      }
    }, 300);
  }

  $("#act-like").addEventListener("click", () => swipe("like"));
  $("#act-nope").addEventListener("click", () => swipe("nope"));
  $("#act-collab").addEventListener("click", () => swipe("collab"));
  $("#deck-reset").addEventListener("click", deal);

  $$(".chip-filter").forEach((chip) =>
    chip.addEventListener("click", () => {
      $$(".chip-filter").forEach((c2) => {
        c2.classList.toggle("is-active", c2 === chip);
        c2.setAttribute("aria-selected", c2 === chip ? "true" : "false");
      });
      state.filter = chip.dataset.filter;
      deal();
    })
  );

  /* Tastatur: Pfeile swipen, Escape schließt */

  document.addEventListener("keydown", (e) => {
    if (!matchModal.hidden && e.key === "Escape") { closeMatch(); return; }
    if (app.hidden || !matchModal.hidden) return;
    if (!$("#convo").hidden && e.key === "Escape") { closeConvo(); return; }
    if (views.discover.hidden) return;
    if (e.key === "ArrowRight") swipe("like");
    if (e.key === "ArrowLeft") swipe("nope");
  });

  /* ── Match ───────────────────────────────────────────────── */

  function createMatch(creator) {
    const m = {
      creator,
      messages: [{ who: "them", text: creator.opener, time: now() }],
      unread: true,
      replyIdx: 0
    };
    state.matches.unshift(m);
    updateCounters();
    return m;
  }

  const heartsBox = $("#match-hearts");

  function spawnHearts() {
    heartsBox.innerHTML = "";
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const colors = ["#ff5747", "#ffb86b", "#ff8f7a", "#f0c37e"];
    for (let i = 0; i < 18; i++) {
      const h = document.createElement("span");
      h.className = "mh";
      h.textContent = "♥";
      h.style.setProperty("--x", 4 + Math.random() * 92 + "%");
      h.style.setProperty("--s", 13 + Math.random() * 15 + "px");
      h.style.setProperty("--d", 2.6 + Math.random() * 1.8 + "s");
      h.style.setProperty("--dl", Math.random() * 1.4 + "s");
      h.style.setProperty("--r", Math.random() * 60 - 30 + "deg");
      h.style.setProperty("--c", colors[i % colors.length]);
      heartsBox.appendChild(h);
    }
  }

  function openMatch(creator) {
    state.pendingMatch = createMatch(creator);
    $("#match-avatar").style.setProperty("--ha", creator.ha);
    $("#match-avatar").style.setProperty("--hb", creator.hb);
    $("#match-avatar").textContent = creator.name[0];
    $("#match-text").textContent = `Du und ${creator.name} — ihr wollt beide mehr als Feeds.`;
    spawnHearts();
    matchModal.hidden = false;
    $("#match-msg").focus();
  }

  function closeMatch() {
    matchModal.hidden = true;
    heartsBox.innerHTML = "";
    state.pendingMatch = null;
  }

  $("#match-continue").addEventListener("click", closeMatch);

  $("#match-msg").addEventListener("click", () => {
    const m = state.pendingMatch;
    matchModal.hidden = true;
    heartsBox.innerHTML = "";
    state.pendingMatch = null;
    showView("chats");
    if (m) openConvo(m);
  });

  function updateCounters() {
    const n = state.matches.filter((m) => m.unread).length;
    const badge = $("#tab-badge");
    badge.hidden = n === 0;
    badge.textContent = n;
    $("#stat-matches").textContent = state.matches.filter((m) => m.creator.id !== "team").length;
  }

  /* ── Chats ───────────────────────────────────────────────── */

  const teamMatch = {
    creator: TEAM_CHAT,
    messages: [{ who: "them", text: TEAM_CHAT.opener, time: now() }],
    unread: true,
    replyIdx: 0
  };
  state.matches.push(teamMatch);

  function renderChatList() {
    const list = $("#chat-list");
    list.innerHTML = "";
    $("#chat-hint").hidden = state.matches.length > 1;

    state.matches.forEach((m) => {
      const c = m.creator;
      const last = m.messages[m.messages.length - 1];
      const li = document.createElement("li");
      li.innerHTML = `
        <button class="chat-item" type="button">
          ${avatarHTML(c, "")}
          <span class="chat-item-main">
            <span class="chat-item-name">${c.name} ${c.verified !== false ? `<span class="verified">${checkSVG}</span>` : ""}</span>
            <span class="chat-item-last">${m.unread ? "● " : ""}${last.text}</span>
          </span>
          <span class="chat-item-time mono">${last.time}</span>
        </button>`;
      $(".chat-item", li).addEventListener("click", () => openConvo(m));
      list.appendChild(li);
    });
    updateCounters();
  }

  const phoneEl = $(".phone");

  function openConvo(m) {
    state.activeChat = m;
    m.unread = false;
    const c = m.creator;
    const av = $("#convo-avatar");
    av.style.setProperty("--ha", c.ha);
    av.style.setProperty("--hb", c.hb);
    av.textContent = c.initial || c.name[0];
    $("#convo-name").textContent = c.name;
    renderBubbles();
    $("#convo").hidden = false;
    phoneEl.classList.add("convo-open");
    updateCounters();
    $("#composer-input").focus();
  }

  function closeConvo() {
    $("#convo").hidden = true;
    phoneEl.classList.remove("convo-open");
    state.activeChat = null;
    renderChatList();
  }

  $("#convo-back").addEventListener("click", closeConvo);

  function renderBubbles() {
    const wrap = $("#bubbles");
    wrap.innerHTML = "";
    state.activeChat.messages.forEach((msg) => {
      const b = document.createElement("div");
      b.className = "bubble " + (msg.who === "me" ? "bubble-me" : "bubble-them");
      b.textContent = msg.text;
      wrap.appendChild(b);
    });
    wrap.scrollTop = wrap.scrollHeight;
  }

  $("#composer").addEventListener("submit", (e) => {
    e.preventDefault();
    const input = $("#composer-input");
    const text = input.value.trim();
    const m = state.activeChat;
    if (!text || !m) return;
    input.value = "";
    m.messages.push({ who: "me", text, time: now() });
    renderBubbles();
    scheduleReply(m);
  });

  function scheduleReply(m) {
    const wrap = $("#bubbles");
    const typing = document.createElement("div");
    typing.className = "bubble-typing";
    typing.innerHTML = "<span></span><span></span><span></span>";

    setTimeout(() => {
      if (state.activeChat !== m) return;
      wrap.appendChild(typing);
      wrap.scrollTop = wrap.scrollHeight;
    }, 500);

    setTimeout(() => {
      typing.remove();
      const pool = m.creator.replies || [];
      const text = m.replyIdx < pool.length
        ? pool[m.replyIdx]
        : GENERIC_REPLIES[(m.replyIdx - pool.length) % GENERIC_REPLIES.length];
      m.replyIdx += 1;
      m.messages.push({ who: "them", text, time: now() });
      if (state.activeChat === m) renderBubbles();
      else { m.unread = true; renderChatList(); }
    }, 1600 + Math.random() * 900);
  }

  /* ── Profil ──────────────────────────────────────────────── */

  $$(".switch").forEach((sw) =>
    sw.addEventListener("click", () => {
      const on = sw.getAttribute("aria-checked") === "true";
      sw.setAttribute("aria-checked", on ? "false" : "true");
    })
  );

  /* ── Scroll-Reveal (Landing) ─────────────────────────────── */

  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          en.target.classList.add("is-visible");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.15 });

    $$("[data-reveal]").forEach((el) => {
      const sibs = $$(":scope > [data-reveal]", el.parentElement);
      el.style.setProperty("--rd", sibs.indexOf(el) * 90 + "ms");
      el.classList.add("reveal-ready");
      io.observe(el);
    });
  }

  /* ── Start ───────────────────────────────────────────────── */

  deal();
  renderChatList();
})();
