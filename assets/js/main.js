/* ============================================================
   ABDUL SAMAD — interaksi halaman
   Konten diedit langsung di index.html. File ini hanya mengurus:
   tema, menu mobile, nav aktif, animasi reveal, form, tombol atas.
   ============================================================ */
(function () {
  "use strict";

  /* --- PENGATURAN FORM ---
     Agar pesan form terkirim otomatis ke email Anda:
     daftar gratis di https://formspree.io, buat form, salin ID dari
     endpoint (https://formspree.io/f/XXXXXXX -> "XXXXXXX") ke bawah ini.
     Jika kosong, form memakai mode cadangan (membuka aplikasi email). */
  const FORMSPREE_ID = "";
  const EMAIL = "abdulsamad257a@gmail.com";

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  /* ---------- Tema terang/gelap (tersimpan) ---------- */
  const root = document.documentElement;
  root.setAttribute("data-theme", localStorage.getItem("theme") || "light");
  $("#themeBtn").addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    root.setAttribute("data-theme", next);
    localStorage.setItem("theme", next);
  });

  /* ---------- Menu mobile ---------- */
  const nav = $("#nav"), navBtn = $("#navBtn");
  navBtn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    navBtn.classList.toggle("x", open);
    navBtn.setAttribute("aria-expanded", open);
  });
  $$("a", nav).forEach((a) =>
    a.addEventListener("click", () => {
      nav.classList.remove("open");
      navBtn.classList.remove("x");
      navBtn.setAttribute("aria-expanded", "false");
    })
  );

  /* ---------- Header on-scroll + nav aktif + tombol ke atas ---------- */
  const head = $("#siteHead"), toTop = $("#toTop");
  const sections = $$("main section[id]");
  const links = $$("#nav a");
  function onScroll() {
    const y = window.scrollY;
    head.classList.toggle("on", y > 10);
    toTop.classList.toggle("on", y > 640);
    let cur = "";
    for (const s of sections) if (y >= s.offsetTop - 110) cur = s.id;
    links.forEach((l) => l.classList.toggle("on", l.getAttribute("href") === "#" + cur));
  }
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  toTop.addEventListener("click", () => scrollTo({ top: 0, behavior: "smooth" }));

  /* ---------- Animasi reveal saat elemen masuk layar ---------- */
  const io = new IntersectionObserver(
    (es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }),
    { threshold: 0.12 }
  );
  $$(".reveal").forEach((el) => io.observe(el));
  /* Jaring pengaman: bila observer tidak berjalan (browser lawas/embedded),
     pastikan konten tetap tampil — jangan pernah biarkan halaman kosong. */
  setTimeout(() => {
    if (!$(".reveal.in")) {
      root.classList.add("no-anim"); // tampil seketika, tanpa menunggu transisi
      $$(".reveal").forEach((el) => el.classList.add("in"));
    }
  }, 1200);

  /* ---------- Form kontak ---------- */
  const form = $("#contactForm"), note = $("#formNote");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(form));
    if (!d.name || !d.email || !d.subject || !d.message) {
      note.classList.add("err");
      note.textContent = "Mohon lengkapi semua kolom.";
      return;
    }

    /* Mode cadangan: buka aplikasi email pengunjung */
    if (!FORMSPREE_ID) {
      const body = `Halo, saya ${d.name}.\n\n${d.message}\n\n— ${d.name} (${d.email})`;
      location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(d.subject)}&body=${encodeURIComponent(body)}`;
      note.classList.remove("err");
      note.textContent = "Aplikasi email Anda akan terbuka.";
      form.reset();
      return;
    }

    /* Kirim langsung via Formspree */
    const btn = $("button[type=submit]", form);
    try {
      btn.disabled = true; btn.textContent = "Mengirim…"; note.textContent = "";
      const res = await fetch(`https://formspree.io/f/${FORMSPREE_ID}`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({ ...d, _subject: d.subject }),
      });
      if (!res.ok) throw 0;
      note.classList.remove("err");
      note.textContent = "Terima kasih — pesan Anda sudah terkirim.";
      form.reset();
    } catch {
      note.classList.add("err");
      note.textContent = "Pesan gagal terkirim. Silakan coba lagi atau lewat WhatsApp.";
    } finally {
      btn.disabled = false; btn.textContent = "Kirim pesan";
    }
  });

  /* ---------- Nomor ghost section (diambil dari .sec__no) ---------- */
  $$(".sec__head").forEach((h) => {
    const no = $(".sec__no", h);
    if (no) h.dataset.n = no.textContent.trim();
  });

  /* ---------- Tanda tangan di konsol ---------- */
  console.log(
    "%c</> Abdul Samad %c— dibangun tanpa framework: HTML · CSS · JS murni",
    "font-weight:bold;color:#E8963E;font-size:13px", "color:#9BA1AC"
  );

  /* ---------- Tahun footer & loader ---------- */
  $("#year").textContent = new Date().getFullYear();
  addEventListener("load", () => setTimeout(() => $("#loader").classList.add("off"), 350));
  setTimeout(() => $("#loader").classList.add("off"), 1800); // cadangan
})();
