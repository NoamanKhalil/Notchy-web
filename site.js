(() => {
  const root = document.documentElement;
  const themeBtn = document.querySelector("[data-theme-toggle]");
  const currentTheme = () => {
    if (root.dataset.theme === "dark" || root.dataset.theme === "light") return root.dataset.theme;
    return matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  };
  const paintTheme = () => {
    const dark = currentTheme() === "dark";
    if (themeBtn) themeBtn.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
    const fav = document.getElementById("favicon");
    if (fav) fav.href = dark ? "/assets/icon/favicon-dark.png" : "/assets/icon/favicon-light.png";
  };
  paintTheme();
  themeBtn?.addEventListener("click", () => {
    const next = currentTheme() === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch (err) {}
    paintTheme();
  });

  const more = document.querySelector("footer .more");
  const rest = document.getElementById("more-guides");
  if (more && rest) {
    more.addEventListener("click", () => {
      const open = more.getAttribute("aria-expanded") === "true";
      more.setAttribute("aria-expanded", String(!open));
      rest.hidden = open;
      more.textContent = open ? "More" : "Less";
    });
  }

  const extra = document.getElementById("blog-more");
  if (extra) {
    extra.addEventListener("click", () => {
      document.querySelectorAll("[data-more]").forEach((item) => { item.hidden = false; });
      const row = extra.closest(".read-more");
      if (row) row.hidden = true;
    });
  }

  document.querySelectorAll("[data-share]").forEach((wrap) => {
    const url = new URL(wrap.dataset.path || location.pathname, location.href).href;
    const title = wrap.dataset.title || document.title;
    const text = encodeURIComponent(title);
    const encoded = encodeURIComponent(url);
    const x = wrap.querySelector("[data-share-x]");
    const li = wrap.querySelector("[data-share-li]");
    const mail = wrap.querySelector("[data-share-mail]");
    if (x) x.href = `https://x.com/intent/post?text=${text}&url=${encoded}`;
    if (li) li.href = `https://www.linkedin.com/sharing/share-offsite/?url=${encoded}`;
    if (mail) mail.href = `mailto:?subject=${text}&body=${encoded}`;
    wrap.querySelector("[data-share-copy]")?.addEventListener("click", async () => {
      const done = wrap.querySelector("[data-share-done]");
      try {
        await navigator.clipboard.writeText(url);
        if (done) done.textContent = "Link copied";
      } catch (err) {
        if (done) done.textContent = "Copy the address from the bar";
      }
    });
  });

  const links = [...document.querySelectorAll(".toc a")];
  if (links.length && "IntersectionObserver" in window) {
    const byId = new Map(links.map((a) => [a.getAttribute("href").slice(1), a]));
    const mark = (id) => links.forEach((a) => a.classList.toggle("is-here", a === byId.get(id)));
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible) mark(visible.target.id);
    }, { rootMargin: "-20% 0px -60% 0px", threshold: [0, 1] });
    byId.forEach((_, id) => {
      const node = document.getElementById(id);
      if (node) observer.observe(node);
    });
  }

  const mac = document.getElementById("mac");
  if (!mac) return;
  const notch = document.getElementById("notch");
  const glow = document.getElementById("glow");
  const hit = document.getElementById("notch-hit");
  const panel = document.getElementById("panel");
  const status = document.getElementById("status");
  const statusText = status.querySelector("span");
  const fs = document.getElementById("fullscreen");
  const read = document.getElementById("glow-read");
  const dot = document.getElementById("demo-pointer");
  const modes = [...document.querySelectorAll(".modes button")];
  let open = false;
  let userDrove = false;
  let restTimer = 0;
  let recTimer = 0;
  let approveTimer = 0;
  let recording = "";
  let recSeconds = 0;
  let focusOn = false;
  let focusLeft = 25 * 60;
  let focusTimer = 0;
  let awake = false;
  let shelf = false;
  let colorI = 0;
  const colors = ["#007AFF", "#30D158", "#FF9F0A", "#FF375F", "#BF5AF2"];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const pad = (n) => String(n).padStart(2, "0");
  const clock = () => {
    const el = document.getElementById("menu-clock");
    if (!el) return;
    el.textContent = new Intl.DateTimeFormat("en-US", {
      weekday: "short", month: "short", day: "numeric", hour: "numeric", minute: "2-digit"
    }).format(new Date());
  };
  clock();
  setInterval(clock, 30000);

  function setStatus(text, kind) {
    status.hidden = false;
    status.dataset.kind = kind || "ok";
    statusText.textContent = text;
    const finder = status.querySelector("[data-act='finder']");
    if (finder) finder.hidden = kind !== "shot";
  }
  function say(text) { if (read) read.textContent = text; }
  function pulse(kind) {
    glow.dataset.pulse = kind;
    clearTimeout(pulse.t);
    pulse.t = setTimeout(() => { delete glow.dataset.pulse; }, 1600);
  }
  function setOpen(next) {
    open = next;
    notch.classList.toggle("is-open", open);
    hit.setAttribute("aria-expanded", String(open));
    panel.setAttribute("aria-hidden", String(!open));
    if ("inert" in panel) panel.inert = !open;
    if (open && dot) dot.hidden = true;
  }
  function glowAmount(t) {
    if (fs.checked) {
      glow.style.setProperty("--g", "0");
      say("Glow off. A full-screen app only opens on click.");
      return;
    }
    glow.style.setProperty("--g", t.toFixed(3));
    say(t < 0.04 ? "Bring the pointer near the notch." : `Glow ${Math.round(t * 100)}%`);
  }
  function stopRec(done) {
    clearInterval(recTimer);
    clearTimeout(approveTimer);
    recTimer = 0;
    recording = "";
    document.querySelectorAll("[data-act='rec']").forEach((btn) => {
      btn.setAttribute("aria-pressed", "false");
      btn.querySelector("small").textContent = btn.dataset.kind === "screen" ? "Screen" : "Area";
    });
    if (done) {
      pulse("green");
      setStatus("Recording stopped", "ok");
    }
  }
  function tickRec() {
    recSeconds += 1;
    const label = `${Math.floor(recSeconds / 60)}:${pad(recSeconds % 60)}`;
    const btn = document.querySelector(`[data-act='rec'][data-kind='${recording}']`);
    if (btn) btn.querySelector("small").textContent = label;
    setStatus(`Recording ${recording === "screen" ? "the screen" : "an area"} · ${label}`, "ok");
  }
  function startRec(kind) {
    clearInterval(recTimer);
    clearTimeout(approveTimer);
    recording = kind;
    recSeconds = 0;
    document.querySelectorAll("[data-act='rec']").forEach((btn) => {
      const on = btn.dataset.kind === kind;
      btn.setAttribute("aria-pressed", String(on));
      btn.querySelector("small").textContent = on ? "Stop" : (btn.dataset.kind === "screen" ? "Screen" : "Area");
    });
    setStatus("Needs approval", "wait");
    pulse("amber");
    approveTimer = setTimeout(() => {
      if (recording !== kind) return;
      delete glow.dataset.pulse;
      tickRec();
      recTimer = setInterval(tickRec, 1000);
    }, reduce ? 0 : 1100);
  }
  function focusLabel() {
    const btn = document.querySelector("[data-act='focus'] small");
    if (!btn) return;
    if (!focusOn && focusLeft === 25 * 60) btn.textContent = "25 min";
    else btn.textContent = `${Math.floor(focusLeft / 60)}:${pad(focusLeft % 60)}`;
  }
  function run(act, kind, name) {
    if (act === "shot") {
      if (recording) stopRec(false);
      const names = { screen: "the whole screen", area: "an area", scroll: "a scrolling page" };
      pulse("green");
      setStatus("Screenshot saved to Desktop", "shot");
      say(`Screenshot of ${names[kind]} saved to Desktop`);
      return;
    }
    if (act === "rec") {
      if (recording === kind) stopRec(true);
      else startRec(kind);
      return;
    }
    if (act === "focus") {
      focusOn = !focusOn;
      clearInterval(focusTimer);
      const btn = document.querySelector("[data-act='focus']");
      btn.setAttribute("aria-pressed", String(focusOn));
      if (focusOn) {
        setStatus("Focus timer running", "ok");
        focusLabel();
        focusTimer = setInterval(() => {
          focusLeft = Math.max(0, focusLeft - 1);
          focusLabel();
          if (focusLeft === 0) {
            clearInterval(focusTimer);
            focusOn = false;
            focusLeft = 25 * 60;
            btn.setAttribute("aria-pressed", "false");
            focusLabel();
            pulse("green");
            setStatus("Focus timer done", "ok");
          }
        }, 1000);
      } else setStatus("Focus timer paused", "ok");
      return;
    }
    if (act === "shelf") {
      shelf = !shelf;
      document.querySelector("[data-act='shelf']").setAttribute("aria-pressed", String(shelf));
      setStatus(shelf ? "On the shelf" : "Shelf cleared", "ok");
      return;
    }
    if (act === "copy") {
      setStatus("Copy text reads type on your screen. This preview does not.", "ok");
      return;
    }
    if (act === "color") {
      const hex = colors[colorI % colors.length];
      colorI += 1;
      setStatus(`Color ${hex}. On your Mac this is the pixel under the pointer.`, "ok");
      return;
    }
    if (act === "qr") {
      setStatus("Scan QR reads a code on screen. This preview does not use a camera.", "ok");
      return;
    }
    if (act === "awake") {
      awake = !awake;
      document.querySelector("[data-act='awake']").setAttribute("aria-pressed", String(awake));
      setStatus(awake ? "Keep awake is on" : "Keep awake is off", "ok");
      return;
    }
    if (act === "clock") {
      const fmt = (tz) => new Intl.DateTimeFormat("en-US", { timeZone: tz, hour: "numeric", minute: "2-digit" }).format(new Date());
      setStatus(`Los Angeles ${fmt("America/Los_Angeles")} · London ${fmt("Europe/London")} · Tokyo ${fmt("Asia/Tokyo")}`, "ok");
      return;
    }
    if (act === "camera") {
      setStatus("Camera mirror is optional. This preview leaves the camera off.", "ok");
      return;
    }
    if (act === "downloads") {
      setStatus("Downloads alerts are optional. This preview does not watch a folder.", "ok");
      return;
    }
    if (act === "meeting") {
      setStatus("Next meeting is optional. This preview does not read a calendar.", "ok");
      return;
    }
    if (act === "settings") {
      setStatus("Settings holds your shortcuts and the optional tools.", "ok");
      return;
    }
    if (act === "app") {
      setStatus(`${name} is a shortcut. This preview does not open it.`, "ok");
      return;
    }
    if (act === "quit") {
      if (recording) stopRec(false);
      setOpen(false);
      status.hidden = true;
      say("Quit closes Notchy. This preview only closed the panel.");
      return;
    }
    if (act === "finder") {
      setStatus("Show in Finder opens the shot on your Mac. This preview has no file.", "ok");
    }
  }

  panel.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;
    userDrove = true;
    run(btn.dataset.act, btn.dataset.kind, btn.dataset.name);
  });
  hit.addEventListener("click", (e) => {
    e.stopPropagation();
    userDrove = true;
    clearTimeout(restTimer);
    setOpen(!open);
  });
  fs.addEventListener("change", () => {
    userDrove = true;
    clearTimeout(restTimer);
    if (fs.checked) {
      glow.style.setProperty("--g", "0");
      delete glow.dataset.pulse;
      say("Glow off. A full-screen app only opens on click.");
      modes.forEach((b) => b.setAttribute("aria-selected", b.dataset.mode === "full" ? "true" : "false"));
    } else glowAmount(0);
  });

  mac.addEventListener("pointermove", (e) => {
    userDrove = true;
    if (dot) dot.hidden = true;
    const r = notch.getBoundingClientRect();
    const dist = Math.hypot(e.clientX - (r.left + r.width / 2), e.clientY - (r.top + r.height / 2));
    const t = Math.max(0, Math.min(1, 1 - dist / 260));
    glowAmount(t);
    clearTimeout(restTimer);
    if (!fs.checked && !open && t > 0.9) restTimer = setTimeout(() => setOpen(true), reduce ? 0 : 380);
  });
  mac.addEventListener("pointerleave", () => {
    clearTimeout(restTimer);
    if (!fs.checked && !glow.dataset.pulse) glowAmount(0);
  });

  modes.forEach((btn) => {
    btn.addEventListener("click", () => {
      userDrove = true;
      modes.forEach((b) => b.setAttribute("aria-selected", String(b === btn)));
      const mode = btn.dataset.mode;
      document.querySelectorAll(".panel [data-group]").forEach((el) => el.classList.toggle("hl", el.dataset.group === mode));
      if (mode === "full") {
        fs.checked = true;
        fs.dispatchEvent(new Event("change"));
        return;
      }
      fs.checked = false;
      setOpen(true);
      if (mode === "glow") {
        setOpen(false);
        glowAmount(1);
        say("Glow 100%. Rest on the notch, or click it, to open the panel.");
      }
      if (mode === "shot") run("shot", "screen");
      if (mode === "rec" && !recording) run("rec", "screen");
    });
  });

  window.addEventListener("keydown", (e) => {
    if (!(e.ctrlKey && e.altKey && e.metaKey)) return;
    const map = { 3: ["shot", "screen"], 4: ["shot", "area"], 7: ["shot", "scroll"], 5: ["rec", "screen"], 6: ["rec", "area"] };
    const hitKey = map[e.key];
    if (!hitKey) return;
    e.preventDefault();
    userDrove = true;
    setOpen(true);
    run(hitKey[0], hitKey[1]);
  });

  if (!reduce) {
    const started = performance.now();
    const step = (now) => {
      if (userDrove) return;
      const p = Math.min(1, (now - started) / 1500);
      if (dot) dot.hidden = false;
      glowAmount(p);
      if (p < 1) requestAnimationFrame(step);
      else {
        if (dot) dot.hidden = true;
        setOpen(true);
      }
    };
    requestAnimationFrame(step);
  } else {
    if (dot) dot.hidden = true;
    say("Bring the pointer near the notch, or click it.");
  }
  if ("inert" in panel) panel.inert = true;
})();
