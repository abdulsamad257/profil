# 🚀 Panduan Deploy — Versi HTML Murni (Statis)

Situs ini statis (tanpa build), jadi sangat mudah di-deploy. Pilih salah satu cara.

---

## A. Netlify Drop (paling cepat — tanpa git, 30 detik)
1. Buka **[app.netlify.com/drop](https://app.netlify.com/drop)**.
2. **Seret folder ini** (`portofolio-website`) ke halaman tersebut.
3. Selesai! Situs langsung online dengan URL gratis. 🎉

## B. Vercel
### Lewat CLI
```bash
npm i -g vercel
vercel            # ikuti prompt (output: situs statis)
vercel --prod
```
### Lewat GitHub
1. Buat repo di **[github.com/new](https://github.com/new)** lalu push:
   ```bash
   git remote add origin https://github.com/USERNAME/portofolio.git
   git branch -M main
   git push -u origin main
   ```
2. Buka **[vercel.com/new](https://vercel.com/new)** → Import repo → **Deploy**.
   (Vercel membaca `vercel.json` untuk URL bersih.)

## C. GitHub Pages
1. Push ke GitHub (lihat langkah di atas).
2. Repo → **Settings → Pages** → Source: `main` / root → **Save**.
3. Situs tampil di `https://USERNAME.github.io/portofolio/`.

---

## ✅ Setelah online
- Perbarui `seo.siteUrl` di [`assets/js/data.js`](assets/js/data.js) dengan domain asli Anda.
- Form kontak Formspree akan berfungsi penuh setelah online (di `file://` lokal tidak bisa).
- Uji preview share di [Facebook Debugger](https://developers.facebook.com/tools/debug/).
