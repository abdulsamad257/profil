/* Generator DAFTAR RIWAYAT HIDUP versi Word (.docx) — tema Biru Profesional.
   Mudah diedit di Microsoft Word / Google Docs.
   Ubah objek DATA di bawah untuk mengganti isi. */
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign,
  TabStopType, TabStopPosition, LevelFormat,
} = require("docx");

// ---------------- DATA (ubah sesuai kebutuhan) ----------------
const DATA = {
  name: "Abdul Samad, S.Kom., M.T.",
  profession: "Web Developer · Data Analyst · AI Enthusiast · IT Consultant",
  personal: [
    ["Tempat, Tgl Lahir", "Makassar, 1 Januari 1997"],
    ["Jenis Kelamin", "Laki-laki"],
    ["Agama", "Islam"],
    ["Status Perkawinan", "Belum Menikah"],
    ["Kewarganegaraan", "Indonesia"],
    ["Telepon / WhatsApp", "+62 812-3456-7890"],
    ["Email", "belajarbersama257a@gmail.com"],
    ["LinkedIn", "linkedin.com/in/username"],
    ["Alamat", "Jl. Contoh No. 123, Kota Makassar, Sulawesi Selatan"],
  ],
  education: [
    ["Magister Teknik Informatika (S2)", "Universitas Contoh Indonesia", "2022 – 2024"],
    ["Sarjana Teknik Informatika (S1)", "Universitas Contoh Indonesia", "2017 – 2021"],
    ["Sekolah Menengah Atas (IPA)", "SMA Negeri Contoh", "2014 – 2017"],
  ],
  experience: [
    ["Freelance Web Developer", "Solusi Digital (Mandiri)", "2022 – Sekarang",
      "Membangun website & aplikasi untuk UMKM, lembaga, dan profesional; dari perancangan, pengembangan, hingga pemeliharaan."],
    ["Data Analyst (Project)", "PT Contoh Analitika", "2021 – 2022",
      "Mengolah & memvisualisasikan data operasional menjadi dashboard interaktif untuk mendukung keputusan bisnis."],
    ["Asisten Penelitian & Penulisan Jurnal", "Laboratorium Kampus", "2020 – 2021",
      "Membantu penelitian, pengumpulan data, dan penyusunan naskah ilmiah hingga terbit di jurnal terindeks."],
  ],
  skills: "Web Development, Frontend & Backend, Database (MySQL), Data Analysis (Python, Power BI), AI Agent, Jaringan Komputer & Mikrotik, Instalasi CCTV, UI/UX Design, Microsoft Office, serta Penulisan Jurnal Ilmiah.",
  certificates: [
    "Web Development Bootcamp — Dicoding (2023)",
    "Data Analysis with Python — Coursera (2023)",
    "Mikrotik Certified Network Associate (MTCNA) — Mikrotik (2022)",
    "Machine Learning — IBM (2023)",
  ],
  signCity: "Makassar",
  signDate: "1 Juli 2026",
};

// ---------------- WARNA (tema Biru Profesional) ----------------
const BLUE = "1D4ED8";   // biru korporat
const NAVY = "1E3A8A";   // navy-blue (header)
const SKY  = "0EA5E9";   // aksen langit
const DARK = "14213D";   // teks utama
const MUTED = "5A6790";  // teks sekunder
const LINE = "D8DEEA";   // garis
const WHITE = "FFFFFF";

const CW = 9026;         // lebar konten (A4, margin 1")
const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE };

// Judul section: teks biru tebal + garis bawah
function heading(text) {
  return new Paragraph({
    spacing: { before: 260, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BLUE, space: 4 } },
    children: [new TextRun({ text: text.toUpperCase(), bold: true, color: BLUE, size: 24, font: "Arial" })],
  });
}

// ---------------- HEADER BANNER (tabel 2 kolom) ----------------
const header = new Table({
  width: { size: CW, type: WidthType.DXA },
  columnWidths: [1600, CW - 1600],
  borders: noBorders,
  rows: [
    new TableRow({
      children: [
        new TableCell({
          width: { size: 1600, type: WidthType.DXA },
          shading: { fill: BLUE, type: ShadingType.CLEAR, color: "auto" },
          verticalAlign: VerticalAlign.CENTER,
          margins: { top: 200, bottom: 200, left: 60, right: 60 },
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: "AS", bold: true, color: WHITE, size: 60, font: "Arial" })],
          })],
        }),
        new TableCell({
          width: { size: CW - 1600, type: WidthType.DXA },
          shading: { fill: NAVY, type: ShadingType.CLEAR, color: "auto" },
          verticalAlign: VerticalAlign.CENTER,
          margins: { top: 160, bottom: 160, left: 240, right: 160 },
          children: [
            new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: "DAFTAR RIWAYAT HIDUP", color: "BFD4FF", size: 16, bold: true, font: "Arial" })] }),
            new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text: DATA.name, color: WHITE, size: 40, bold: true, font: "Arial" })] }),
            new Paragraph({ children: [new TextRun({ text: DATA.profession, color: "E6ECFF", size: 19, font: "Arial" })] }),
          ],
        }),
      ],
    }),
  ],
});

// ---------------- DATA PRIBADI (tabel label : nilai) ----------------
const dpRows = DATA.personal.map(([label, value]) =>
  new TableRow({
    children: [
      new TableCell({
        width: { size: 2400, type: WidthType.DXA }, borders: noBorders,
        margins: { top: 30, bottom: 30, left: 0, right: 60 },
        children: [new Paragraph({ children: [
          new TextRun({ text: label, bold: true, color: MUTED, size: 19, font: "Arial" }),
        ] })],
      }),
      new TableCell({
        width: { size: 300, type: WidthType.DXA }, borders: noBorders,
        margins: { top: 30, bottom: 30, left: 0, right: 0 },
        children: [new Paragraph({ children: [new TextRun({ text: ":", color: MUTED, size: 19, font: "Arial" })] })],
      }),
      new TableCell({
        width: { size: CW - 2700, type: WidthType.DXA }, borders: noBorders,
        margins: { top: 30, bottom: 30, left: 60, right: 0 },
        children: [new Paragraph({ children: [
          new TextRun({ text: value, color: DARK, size: 19, font: "Arial" }),
        ] })],
      }),
    ],
  })
);
const dataPribadi = new Table({
  width: { size: CW, type: WidthType.DXA },
  columnWidths: [2400, 300, CW - 2700],
  borders: noBorders,
  rows: dpRows,
});

// ---------------- BAGIAN TEKS ----------------
const body = [];

// Pendidikan
body.push(heading("Riwayat Pendidikan"));
DATA.education.forEach(([prog, school, year]) => {
  body.push(new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: CW }],
    spacing: { before: 40 },
    children: [
      new TextRun({ text: prog, bold: true, color: DARK, size: 20, font: "Arial" }),
      new TextRun({ text: `\t${year}`, italics: true, color: BLUE, size: 17, font: "Arial" }),
    ],
  }));
  body.push(new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: school, color: MUTED, size: 18, font: "Arial" })] }));
});

// Pengalaman
body.push(heading("Pengalaman"));
DATA.experience.forEach(([role, comp, year, desc]) => {
  body.push(new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: CW }],
    spacing: { before: 60 },
    children: [
      new TextRun({ text: role, bold: true, color: DARK, size: 20, font: "Arial" }),
      new TextRun({ text: `\t${year}`, italics: true, color: BLUE, size: 17, font: "Arial" }),
    ],
  }));
  body.push(new Paragraph({ children: [new TextRun({ text: comp, bold: true, color: SKY, size: 18, font: "Arial" })] }));
  body.push(new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: desc, color: MUTED, size: 18, font: "Arial" })] }));
});

// Keahlian
body.push(heading("Keahlian"));
body.push(new Paragraph({
  alignment: AlignmentType.JUSTIFIED, spacing: { before: 40 },
  children: [new TextRun({ text: DATA.skills, color: DARK, size: 19, font: "Arial" })],
}));

// Pelatihan & Sertifikat (bullet)
body.push(heading("Pelatihan & Sertifikat"));
DATA.certificates.forEach((cert) => {
  body.push(new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { before: 20 },
    children: [new TextRun({ text: cert, color: DARK, size: 19, font: "Arial" })],
  }));
});

// Penutup + tanda tangan
body.push(new Paragraph({ spacing: { before: 300 }, children: [new TextRun({ text: "Demikian daftar riwayat hidup ini saya buat dengan sebenar-benarnya.", italics: true, color: MUTED, size: 18, font: "Arial" })] }));
body.push(new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { before: 160 }, children: [new TextRun({ text: `${DATA.signCity}, ${DATA.signDate}`, color: DARK, size: 19, font: "Arial" })] }));
body.push(new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: "Hormat saya,", color: DARK, size: 19, font: "Arial" })] }));
body.push(new Paragraph({ children: [new TextRun({ text: "" })] }));
body.push(new Paragraph({ children: [new TextRun({ text: "" })] }));
body.push(new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: DATA.name, bold: true, color: BLUE, size: 20, underline: {}, font: "Arial" })] }));

// ---------------- DOKUMEN ----------------
const doc = new Document({
  styles: { default: { document: { run: { font: "Arial", size: 20 } } } },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 220 } } } }],
    }],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children: [
      header,
      new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: "" })] }),
      heading("Data Pribadi"),
      dataPribadi,
      ...body,
    ],
  }],
});

const OUT = [
  "C:/Users/samad/Music/Berkas Abdul Samad/portofolio-nextjs/public/files/Daftar-Riwayat-Hidup-Abdul-Samad.docx",
  "C:/Users/samad/Music/Berkas Abdul Samad/portofolio-website/files/Daftar-Riwayat-Hidup-Abdul-Samad.docx",
];
Packer.toBuffer(doc).then((buf) => {
  OUT.forEach((p) => { fs.writeFileSync(p, buf); console.log("OK ->", p); });
});
