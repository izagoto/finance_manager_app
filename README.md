### 💰 Finance Management App

Aplikasi manajemen keuangan pribadi dan tim dengan fitur lengkap untuk mencatat **pemasukan**, **pengeluaran**, **investasi**, serta **dashboard analitik**, dan **ekspor laporan ke PDF dan Excel**. Admin juga dapat mengelola pengguna dan peran.

---

## ✅ TO DO - Finance Management App

### 🔐 Fitur Autentikasi & Manajemen Pengguna

- ✅ Login dengan JWT
- ✅ Logout dengan token blacklist
- ✅ Token decoding untuk autentikasi pengguna
- ✅ Role-based Access Control: Admin & User
- ✅ CRUD User (oleh Admin)

### 💸 Fitur Keuangan (Pemasukan, Pengeluaran, Investasi)

- 🚧 Input Pemasukan
- 🚧 Riwayat dan detail Pemasukan
- 🚧 Input Pengeluaran
- 🚧 Riwayat dan detail Pengeluaran
- 🚧 Input & Manajemen Investasi
- 🚧 Riwayat dan laporan Investasi
- 🚧 Dashboard Ringkasan Keuangan
- 🚧 Grafik interaktif pemasukan/pengeluaran/investasi

### 📤 Ekspor Data & Laporan

- 🚧 Ekspor transaksi ke PDF
- 🚧 Ekspor transaksi ke Excel
- 🚧 Filter transaksi berdasarkan tanggal, kategori, dan jenis transaksi
- 🚧 Fitur pencarian berdasarkan nama transaksi, deskripsi, atau kategori

### 🖥️ UI & UX

- 🚧 Tampilan responsif untuk desktop dan mobile (React + Bootstrap)
- 🚧 Navigasi antar halaman yang intuitif
- 🚧 Formulir validasi dan pesan kesalahan
- 🚧 Notifikasi sukses/gagal (toast/alert)

---

## 🚀 Fitur Utama

- ✅ Autentikasi dan otorisasi (Login, Logout, Token JWT)
- ✅ Role-based Access Control: `Admin` dan `User`
- ✅ CRUD User (oleh Admin)
- ✅ Input & Riwayat **Pemasukan**
- ✅ Input & Riwayat **Pengeluaran**
- ✅ Manajemen **Investasi**
- ✅ Dashboard Ringkasan Keuangan
- ✅ Grafik Interaktif (pemasukan/pengeluaran/investasi)
- ✅ Ekspor data ke **PDF** dan **Excel**
- ✅ Responsif dan modern UI (React + Bootstrap)

---

## 🧱 Teknologi yang Digunakan

### Backend

- [FastAPI](https://fastapi.tiangolo.com/)
- SQLite (bisa dengan PostgreSQL/MySQL)
- SQLAlchemy ORM
- Pydantic
- JWT Authentication
- Uvicorn

### Frontend

- React.js (Vite)
- Bootstrap + MDB React UI Kit
- Axios (komunikasi API)

---

## ⚙️ Instalasi & Menjalankan Aplikasi

### 1. Clone Project

```bash
git clone https://github.com/username/finance-management-app.git
cd finance-management-app
```

### 2. Jalankan Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Jalankan server
uvicorn app.main:app --reload
```

### 3. Jalankan Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

---

## 🛢️ Database

Secara default menggunakan **SQLite**, namun dapat dengan mudah diganti ke PostgreSQL atau MySQL dengan mengatur variabel di `.env`:

```env
DATABASE_URL=sqlite:///./app.db
```

Contoh untuk PostgreSQL:

```env
DATABASE_URL=postgresql://username:password@localhost/dbname
```

---

## 🔐 Akun Default (Seeded)

| Role  | Username | Password |
| ----- | -------- | -------- |
| Admin | admin    | admin123 |
| User  | user     | user123  |

---

## 📄 Lisensi

Proyek ini dirilis dengan lisensi MIT. Bebas digunakan dan dimodifikasi sesuai kebutuhan.

---

## ✨ Kontribusi

Pull request dipersilakan! Jangan lupa beri ⭐ jika kamu suka proyek ini 😄
