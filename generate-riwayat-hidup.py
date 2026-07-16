# -*- coding: utf-8 -*-
"""
Generator DAFTAR RIWAYAT HIDUP (PDF) dengan header banner gradien.
Tema warna serasi website: navy + ungu + cyan + gold.

CARA PAKAI:
  1. pip install reportlab
  2. python generate-riwayat-hidup.py
  Hasil: Daftar-Riwayat-Hidup-Abdul-Samad.pdf di folder files/ (otomatis terdeteksi).

EDIT DATA cukup pada bagian D = {...} di bawah (ganti tanggal lahir, alamat, dll).
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth

# ---------------- DATA (ubah sesuai kebutuhan) ----------------
D = {
    "name": "Abdul Samad, S.Kom., M.T.",
    "profession": "Web Developer · Data Analyst · AI Enthusiast · IT Consultant",
    "personal": [
        ("Tempat, Tgl Lahir", "Makassar, 1 Januari 1997"),
        ("Jenis Kelamin", "Laki-laki"),
        ("Agama", "Islam"),
        ("Status Perkawinan", "Belum Menikah"),
        ("Kewarganegaraan", "Indonesia"),
        ("Telepon / WhatsApp", "+62 812-3456-7890"),
        ("Email", "belajarbersama257a@gmail.com"),
        ("LinkedIn", "linkedin.com/in/username"),
    ],
    "address": "Jl. Contoh No. 123, Kota Makassar, Sulawesi Selatan",
    "education": [
        ("Magister Teknik Informatika (S2)", "Universitas Contoh Indonesia", "2022 – 2024"),
        ("Sarjana Teknik Informatika (S1)", "Universitas Contoh Indonesia", "2017 – 2021"),
        ("Sekolah Menengah Atas (IPA)", "SMA Negeri Contoh", "2014 – 2017"),
    ],
    "experience": [
        ("Freelance Web Developer", "Solusi Digital (Mandiri)", "2022 – Sekarang",
         "Membangun website & aplikasi untuk UMKM, lembaga, dan profesional; dari perancangan, pengembangan, hingga pemeliharaan."),
        ("Data Analyst (Project)", "PT Contoh Analitika", "2021 – 2022",
         "Mengolah & memvisualisasikan data operasional menjadi dashboard interaktif untuk mendukung keputusan bisnis."),
        ("Asisten Penelitian & Penulisan Jurnal", "Laboratorium Kampus", "2020 – 2021",
         "Membantu penelitian, pengumpulan data, dan penyusunan naskah ilmiah hingga terbit di jurnal terindeks."),
    ],
    "skills": ("Web Development, Frontend & Backend, Database (MySQL), Data Analysis (Python, "
               "Power BI), AI Agent, Jaringan Komputer & Mikrotik, Instalasi CCTV, UI/UX Design, "
               "Microsoft Office, serta Penulisan Jurnal Ilmiah."),
    "certificates": [
        "Web Development Bootcamp — Dicoding (2023)",
        "Data Analysis with Python — Coursera (2023)",
        "Mikrotik Certified Network Associate (MTCNA) — Mikrotik (2022)",
        "Machine Learning — IBM (2023)",
    ],
    "sign_city": "Makassar",
    "sign_date": "1 Juli 2026",
    "sign_name": "Abdul Samad, S.Kom., M.T.",
}

# ---------------- WARNA (tema: Biru Profesional) ----------------
# Ganti nilai hex di bawah untuk mengubah tema warna dokumen.
PURPLE  = HexColor(0x1D4ED8)   # biru korporat — aksen utama (judul, garis section)
PURPLE2 = HexColor(0x1E3A8A)   # navy-blue — sisi gelap banner & monogram
CYAN    = HexColor(0x38BDF8)   # sky — sisi terang banner & teks tahun
GOLD    = HexColor(0x0EA5E9)   # sky-500 — garis aksen di bawah banner
DARK    = HexColor(0x14213D)   # teks utama
MUTED   = HexColor(0x5A6790)   # teks sekunder
LINE    = HexColor(0xE2E6F0)   # garis pemisah

W, H = A4
LM, RM = 45, 45
CW = W - LM - RM


def sty(size, color, leading=None, bold=False, align=0):
    return ParagraphStyle("s", fontName="Helvetica-Bold" if bold else "Helvetica",
                          fontSize=size, textColor=color, leading=leading or size * 1.32, alignment=align)


def para(c, text, st, x, y_top, width):
    p = Paragraph(text, st)
    _, h = p.wrap(width, 3000)
    p.drawOn(c, x, y_top - h)
    return h


def hgrad(c, x, y, w, h, c1, c2, steps=140):
    for i in range(steps):
        t = i / (steps - 1)
        c.setFillColorRGB(c1.red + (c2.red - c1.red) * t,
                          c1.green + (c2.green - c1.green) * t,
                          c1.blue + (c2.blue - c1.blue) * t)
        c.rect(x + w * i / steps, y, w / steps + 0.6, h, fill=1, stroke=0)


def build(path):
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle(f"Daftar Riwayat Hidup — {D['name']}")
    c.setAuthor(D["name"])

    # ---------- HEADER BANNER ----------
    bh = 150
    hgrad(c, 0, H - bh, W, bh, PURPLE2, CYAN)
    c.setFillColorRGB(0, 0, 0.06, 0.18); c.rect(0, H - bh, W, bh, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(0, H - bh - 4, W, 4, fill=1, stroke=0)

    mcx, mcy = LM + 44, H - bh / 2
    c.setFillColor(white); c.circle(mcx, mcy, 46, fill=1, stroke=0)
    c.setStrokeColor(white); c.setLineWidth(2); c.circle(mcx, mcy, 52, fill=0, stroke=1)
    c.setFillColor(PURPLE2); c.setFont("Helvetica-Bold", 34)
    initials = "".join(w[0] for w in D["name"].replace(",", "").split()[:2]).upper()
    c.drawCentredString(mcx, mcy - 12, initials)

    tx = mcx + 78
    c.setFillColor(HexColor(0xEAF6FF)); c.setFont("Helvetica-Bold", 9)
    c.drawString(tx, H - 52, "D A F T A R   R I W A Y A T   H I D U P")
    c.setFillColor(white); c.setFont("Helvetica-Bold", 22)
    c.drawString(tx, H - 82, D["name"])
    c.setFillColor(HexColor(0xE6ECFF)); c.setFont("Helvetica", 10.5)
    c.drawString(tx, H - 102, D["profession"])

    # ---------- BODY ----------
    y = H - bh - 30

    def heading(text, y):
        c.setFillColor(PURPLE); c.rect(LM, y - 2, 4, 14, fill=1, stroke=0)
        c.setFillColor(DARK); c.setFont("Helvetica-Bold", 12)
        c.drawString(LM + 12, y, text.upper())
        c.setStrokeColor(LINE); c.setLineWidth(1); c.line(LM, y - 8, LM + CW, y - 8)
        return y - 24

    # DATA PRIBADI
    y = heading("Data Pribadi", y)
    col_w = CW / 2
    label_w = 92
    rows = D["personal"]
    half = (len(rows) + 1) // 2
    cols = [rows[:half], rows[half:]]
    row_h = 17
    start_y = y
    for ci, colrows in enumerate(cols):
        cx = LM + ci * (col_w + 6)
        yy = start_y
        for label, value in colrows:
            c.setFillColor(MUTED); c.setFont("Helvetica-Bold", 8.4); c.drawString(cx, yy, label)
            c.drawString(cx + label_w - 8, yy, ":")
            c.setFillColor(DARK); c.setFont("Helvetica", 8.6); c.drawString(cx + label_w, yy, value)
            yy -= row_h
    y = start_y - half * row_h - 2
    c.setFillColor(MUTED); c.setFont("Helvetica-Bold", 8.4); c.drawString(LM, y, "Alamat")
    c.drawString(LM + label_w - 8, y, ":")
    c.setFillColor(DARK); c.setFont("Helvetica", 8.6); c.drawString(LM + label_w, y, D["address"])
    y -= 24

    # RIWAYAT PENDIDIKAN
    y = heading("Riwayat Pendidikan", y)
    for prog, school, year in D["education"]:
        c.setFillColor(DARK); c.setFont("Helvetica-Bold", 9.6); c.drawString(LM + 4, y, prog)
        c.setFillColor(PURPLE2); c.setFont("Helvetica-Oblique", 8.2); c.drawRightString(LM + CW, y, year)
        y -= 12
        c.setFillColor(MUTED); c.setFont("Helvetica", 8.4); c.drawString(LM + 4, y, school)
        y -= 17
    y -= 6

    # PENGALAMAN
    y = heading("Pengalaman", y)
    for role, comp, year, desc in D["experience"]:
        c.setFillColor(DARK); c.setFont("Helvetica-Bold", 9.8); c.drawString(LM + 4, y, role)
        c.setFillColor(PURPLE2); c.setFont("Helvetica-Oblique", 8.2); c.drawRightString(LM + CW, y, year)
        y -= 12
        c.setFillColor(HexColor(0x0369A1)); c.setFont("Helvetica-Bold", 8.4); c.drawString(LM + 4, y, comp)
        y -= 12
        y -= para(c, desc, sty(8.4, MUTED, leading=11.5), LM + 4, y, CW - 4) + 13
    y -= 2

    # KEAHLIAN
    y = heading("Keahlian", y)
    y -= para(c, D["skills"], sty(8.8, DARK, leading=13, align=4), LM + 4, y, CW - 4) + 16

    # PELATIHAN & SERTIFIKAT
    y = heading("Pelatihan & Sertifikat", y)
    for cert in D["certificates"]:
        y -= para(c, "•&nbsp;&nbsp;" + cert, sty(8.6, DARK, leading=12), LM + 4, y, CW - 4) + 5
    y -= 12

    # TANDA TANGAN
    c.setFillColor(MUTED); c.setFont("Helvetica-Oblique", 8.5)
    c.drawString(LM + 4, y, "Demikian daftar riwayat hidup ini saya buat dengan sebenar-benarnya.")
    sx = LM + CW - 170
    c.setFillColor(DARK); c.setFont("Helvetica", 9)
    c.drawCentredString(sx + 85, y - 4, f"{D['sign_city']}, {D['sign_date']}")
    c.drawCentredString(sx + 85, y - 16, "Hormat saya,")
    c.setStrokeColor(LINE); c.setLineWidth(1); c.line(sx + 10, y - 58, sx + 160, y - 58)
    c.setFillColor(PURPLE2); c.setFont("Helvetica-Bold", 9.6)
    c.drawCentredString(sx + 85, y - 70, D["sign_name"])

    c.showPage(); c.save()
    print("Daftar Riwayat Hidup dibuat ->", path)


if __name__ == "__main__":
    out_dir = "public/files" if os.path.isdir("public") else "files"
    os.makedirs(out_dir, exist_ok=True)
    build(os.path.join(out_dir, "Daftar-Riwayat-Hidup-Abdul-Samad.pdf"))
