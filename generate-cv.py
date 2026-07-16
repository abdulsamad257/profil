# -*- coding: utf-8 -*-
"""
Generator CV PDF satu halaman, dua kolom, bertema sesuai website
(navy + aksen ungu/cyan/gold).

CARA PAKAI:
  1. pip install reportlab
  2. python generate-cv.py
  Hasil: CV-Abdul-Samad.pdf di folder files/ (otomatis terdeteksi).

EDIT DATA CV cukup pada bagian DATA = {...} di bawah.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth

# ---------------- DATA (ubah sesuai kebutuhan) ----------------
DATA = {
    "name": "Abdul Samad",
    "degree": "S.Kom., M.T.",
    "profession": "Web Developer · Data Analyst · AI Enthusiast · IT Consultant",
    "profile": ("Profesional teknologi dengan minat kuat pada pengembangan web, analisis data, "
                "dan kecerdasan buatan. Berlatar pendidikan S2 teknik, terbiasa menerjemahkan "
                "kebutuhan nyata menjadi solusi digital yang rapi, terukur, dan mudah digunakan. "
                "Aktif mengembangkan AI Agent serta menangani jaringan dan keamanan (Mikrotik & CCTV)."),
    "contact": [
        ("Email", "belajarbersama257a@gmail.com"),
        ("WhatsApp", "+62 812-3456-7890"),
        ("Lokasi", "Makassar, Indonesia"),
        ("LinkedIn", "linkedin.com/in/username"),
        ("GitHub", "github.com/username"),
    ],
    "skills": [
        ("Web Development", 92), ("Frontend", 90), ("Backend", 85),
        ("Database", 84), ("Data Analysis", 86), ("AI Agent", 82),
        ("Jaringan & Mikrotik", 83), ("CCTV", 81),
        ("UI/UX Design", 80), ("Microsoft Office", 95),
    ],
    "experience": [
        ("Freelance Web Developer", "Solusi Digital (Mandiri)", "2022 – Sekarang",
         "Membangun website & aplikasi untuk UMKM, lembaga, dan profesional; dari perancangan, pengembangan, hingga pemeliharaan.",
         "HTML · CSS · JavaScript · PHP · Laravel · MySQL"),
        ("Data Analyst (Project)", "PT Contoh Analitika", "2021 – 2022",
         "Mengolah & memvisualisasikan data operasional menjadi dashboard interaktif untuk mendukung keputusan.",
         "Python · Pandas · Power BI · SQL"),
        ("Asisten Penelitian & Jurnal", "Laboratorium Kampus", "2020 – 2021",
         "Membantu penelitian, pengumpulan data, dan penyusunan naskah ilmiah hingga terbit di jurnal terindeks.",
         "LaTeX · Mendeley · SPSS"),
    ],
    "education": [
        ("Magister Teknik Informatika (S2)", "Universitas Contoh Indonesia", "2022 – 2024"),
        ("Sarjana Teknik Informatika (S1)", "Universitas Contoh Indonesia", "2017 – 2021"),
    ],
    "certificates": [
        "Web Development Bootcamp — Dicoding (2023)",
        "Data Analysis with Python — Coursera (2023)",
        "Mikrotik Certified MTCNA — Mikrotik (2022)",
    ],
}

# ---------------- WARNA & TATA LETAK ----------------
NAVY    = HexColor(0x0B1230)   # sidebar
NAVY2   = HexColor(0x26305A)   # track bar skill
PURPLE  = HexColor(0x7C5CFF)
PURPLE2 = HexColor(0x5B3DF0)
CYAN    = HexColor(0x22D3EE)
GOLD    = HexColor(0xF6C453)
DARK    = HexColor(0x15203F)   # teks utama di area putih
MUTED   = HexColor(0x5A6790)
SIDEMUT = HexColor(0x9AA5CC)   # teks redup di sidebar

W, H = A4                      # 595.27 x 841.89
SB_W = 200                     # lebar sidebar
SBX  = 22                      # margin kiri sidebar
SBW  = SB_W - SBX - 18         # lebar konten sidebar
MX   = SB_W + 26               # x kolom utama
MW   = W - MX - 26             # lebar kolom utama


def style(size, color, leading=None, bold=False):
    return ParagraphStyle(
        "s", fontName="Helvetica-Bold" if bold else "Helvetica",
        fontSize=size, textColor=color, leading=leading or size * 1.3,
    )


def para(c, text, st, x, y_top, width):
    """Gambar paragraf dengan wrapping; kembalikan tinggi terpakai."""
    p = Paragraph(text, st)
    _, h = p.wrap(width, 2000)
    p.drawOn(c, x, y_top - h)
    return h


def build(path):
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle(f"CV — {DATA['name']}")
    c.setAuthor(DATA["name"])

    # Latar sidebar + aksen
    c.setFillColor(NAVY); c.rect(0, 0, SB_W, H, fill=1, stroke=0)
    c.setFillColor(PURPLE2); c.rect(SB_W - 3, 0, 3, H, fill=1, stroke=0)
    c.setFillColor(CYAN); c.rect(SB_W, H - 5, W - SB_W, 5, fill=1, stroke=0)

    # Monogram
    cx, cy = SB_W / 2, H - 78
    c.setStrokeColor(CYAN); c.setLineWidth(2); c.circle(cx, cy, 44, stroke=1, fill=0)
    c.setFillColor(PURPLE); c.circle(cx, cy, 37, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 30)
    initials = "".join(w[0] for w in DATA["name"].split()[:2]).upper()
    c.drawCentredString(cx, cy - 10, initials)

    # ---- Sidebar ----
    def side_heading(text, y):
        c.setFillColor(CYAN); c.setFont("Helvetica-Bold", 10)
        c.drawString(SBX, y, text.upper())
        c.setStrokeColor(HexColor(0x2A3560)); c.setLineWidth(1)
        c.line(SBX, y - 6, SBX + SBW, y - 6)
        return y - 22

    y = H - 150
    y = side_heading("Kontak", y)
    for label, value in DATA["contact"]:
        c.setFillColor(SIDEMUT); c.setFont("Helvetica", 6.8)
        c.drawString(SBX, y, label.upper())
        c.setFillColor(white)
        fs = 8.2
        while stringWidth(value, "Helvetica", fs) > SBW and fs > 6.5:
            fs -= 0.2
        c.setFont("Helvetica", fs); c.drawString(SBX, y - 11, value)
        y -= 27

    y -= 6
    y = side_heading("Keahlian", y)
    for name, lvl in DATA["skills"]:
        c.setFillColor(white); c.setFont("Helvetica", 8.3); c.drawString(SBX, y, name)
        c.setFillColor(SIDEMUT); c.setFont("Helvetica", 7); c.drawRightString(SBX + SBW, y, f"{lvl}%")
        by = y - 7
        c.setFillColor(NAVY2); c.rect(SBX, by, SBW, 3.2, fill=1, stroke=0)
        c.setFillColor(CYAN); c.rect(SBX, by, SBW * lvl / 100.0, 3.2, fill=1, stroke=0)
        y -= 21

    y -= 6
    y = side_heading("Sertifikat", y)
    for cert in DATA["certificates"]:
        y -= para(c, "• " + cert, style(7.6, SIDEMUT, leading=10), SBX, y, SBW) + 6

    # ---- Kolom utama ----
    ym = H - 70
    c.setFillColor(DARK); c.setFont("Helvetica-Bold", 25); c.drawString(MX, ym, DATA["name"])
    c.setFillColor(MUTED); c.setFont("Helvetica", 11)
    c.drawString(MX + stringWidth(DATA["name"], "Helvetica-Bold", 25) + 8, ym + 2, DATA["degree"])
    ym -= 20
    c.setFillColor(PURPLE2); c.setFont("Helvetica-Bold", 10.5); c.drawString(MX, ym, DATA["profession"])
    ym -= 10
    c.setFillColor(GOLD); c.rect(MX, ym, 54, 3, fill=1, stroke=0)
    ym -= 18

    def main_heading(text, y):
        c.setFillColor(PURPLE); c.rect(MX, y - 1, 4, 13, fill=1, stroke=0)
        c.setFillColor(DARK); c.setFont("Helvetica-Bold", 11.5); c.drawString(MX + 11, y, text.upper())
        return y - 18

    ym = main_heading("Profil", ym)
    ym -= para(c, DATA["profile"], style(8.8, MUTED, leading=12.6), MX, ym, MW) + 16

    ym = main_heading("Pengalaman", ym)
    for role, comp, year, desc, tools in DATA["experience"]:
        c.setFillColor(DARK); c.setFont("Helvetica-Bold", 10.3); c.drawString(MX, ym, role)
        c.setFillColor(MUTED); c.setFont("Helvetica-Oblique", 8); c.drawRightString(MX + MW, ym, year)
        ym -= 12
        c.setFillColor(PURPLE2); c.setFont("Helvetica-Bold", 8.6); c.drawString(MX, ym, comp)
        ym -= 13
        ym -= para(c, desc, style(8.4, MUTED, leading=11.8), MX, ym, MW)
        ym -= 12
        c.setFillColor(HexColor(0x7A86AE)); c.setFont("Helvetica", 7.4); c.drawString(MX, ym, tools)
        ym -= 21

    ym -= 2
    ym = main_heading("Pendidikan", ym)
    for prog, school, year in DATA["education"]:
        c.setFillColor(DARK); c.setFont("Helvetica-Bold", 9.8); c.drawString(MX, ym, prog)
        c.setFillColor(MUTED); c.setFont("Helvetica-Oblique", 8); c.drawRightString(MX + MW, ym, year)
        ym -= 12
        c.setFillColor(CYAN); c.setFont("Helvetica", 8.4); c.drawString(MX, ym, school)
        ym -= 20

    c.setFillColor(MUTED); c.setFont("Helvetica", 7)
    c.drawString(MX, 28, "Dibuat dengan profil portofolio digital — namaanda.com")

    c.showPage(); c.save()
    print("CV dibuat ->", path)


if __name__ == "__main__":
    # Deteksi folder output otomatis (Next.js: public/files, HTML: files)
    out_dir = "public/files" if os.path.isdir("public") else "files"
    os.makedirs(out_dir, exist_ok=True)
    build(os.path.join(out_dir, "CV-Abdul-Samad.pdf"))
