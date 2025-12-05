# Pbo
# 🍽️ Django Food Ordering System  
Project akhir mata kuliah PBO – Sistem pemesanan makanan dengan role: Admin, Customer, Driver, dan Resto.

---

## 📌 1. Fitur Utama
- **Admin:** kelola user, kelola data, kontrol sistem  
- **Customer:** pesan makanan, lihat status pesanan  
- **Driver:** ambil order, update status pengantaran  
- **Resto:** kelola menu, terima pesanan, update status  

---

## 📁 2. Struktur Folder Project
Pastikan struktur folder seperti ini:


---

## 🚀 3. Cara Menjalankan Project

### **Step 1 — Clone Repo**
```bash
git clone https://github.com/EllNoStrong/Pbo.git
cd Pbo

2. Buat Virtual Environment
Windows:
python -m venv venv
venv\Scripts\activate

MacOS / Linux:
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Migrate Database
python manage.py migrate

5. Jalankan Server
python manage.py runserver


Akses melalui:

http://127.0.0.1:8000/

🔐 Akun Superuser (Admin Panel)

Login admin:

Username: adminpanel
Password: admin123


URL Admin:

http://127.0.0.1:8000/admin/

❗ Catatan Penting

Jangan push venv/

Jangan push db.sqlite3

Update selalu requirements.txt dengan:

pip freeze > requirements.txt

👨‍💻 Developer

Marcellino Rafael
Teknik Elektro – Universitas Negeri Semarang
