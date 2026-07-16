# Website Profil Pribadi — Abdul Samad

Website personal branding satu halaman: **IT Support · Teknisi Jaringan · Administrasi Digital**.
Dibangun dengan HTML, CSS, dan JavaScript murni — tanpa framework, tanpa proses build.
Seluruh konten diambil dari data asli (CV ABDUL SAMAD.pdf).

## Struktur

```
portofolio-website/
├── index.html            # SELURUH KONTEN ada di sini (semantic HTML + SEO)
├── assets/
│   ├── css/style.css     # Desain (tema terang/gelap, responsif)
│   ├── js/main.js        # Interaksi (tema, menu, reveal, form) + FORMSPREE_ID
│   └── img/              # profile.png, og-image.png, favicon
└── files/
    └── CV-Abdul-Samad.pdf  # CV asli untuk tombol "Unduh CV"
```

## Menjalankan

Klik dua kali `index.html`, atau lebih baik lewat server lokal:

```bash
python -m http.server 5500    # lalu buka http://localhost:5500
```

## Mengedit

| Yang ingin diubah | Lokasi |
|---|---|
| Teks/konten apa pun | `index.html` — cari section-nya (01–06), edit langsung |
| Warna & tipografi | `assets/css/style.css` bagian token `:root` / `[data-theme]` |
| Form kontak (kirim otomatis) | `assets/js/main.js` → isi `FORMSPREE_ID` (gratis di formspree.io) |
| Foto profil | Ganti `assets/img/profile.png` (PNG transparan lebih bagus) |
| CV | Ganti `files/CV-Abdul-Samad.pdf` |

## Deploy

- **Netlify Drop** (tercepat): seret folder ini ke app.netlify.com/drop
- **Vercel / GitHub Pages**: lihat `DEPLOY.md`

Setelah online: isi `og:url` di `index.html` dengan domain Anda, dan uji preview share
di Facebook Sharing Debugger / LinkedIn Post Inspector.
