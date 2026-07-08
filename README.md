````markdown
# Test Backend - Sharing Vision


# Installation

Clone repository

```bash
git clone <repository-url>
cd test_backend
```

Create Virtual Environment

macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependency

```bash
pip install -r requirements.txt
```


# Database

Project ini menggunakan MySQL dari XAMPP.

Pastikan service **MySQL** sudah berjalan.

Buat database baru

```sql
CREATE DATABASE test_backend_anjar;
```

# Environment Configuration

Buat file `.env`

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=test_backend_anjar
DB_USER=root
DB_PASSWORD=
```

Sesuaikan jika menggunakan user/password MySQL yang berbeda.

---

# Database Migration

Generate migration

```bash
alembic revision --autogenerate -m "create posts table"
```

Jalankan migration

```bash
alembic upgrade head
```

Setelah berhasil, database akan memiliki tabel

- posts
- alembic_version

---

# Run Application

Menjalankan development server

```bash
uvicorn app.main:app --reload --port 8999
```

Server akan berjalan di

```
http://127.0.0.1:8999
```

````
