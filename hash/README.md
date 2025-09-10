Oke, aku bikin README.md versi **1 kolom rapi** jadi tinggal copy-paste tanpa perlu select manual di banyak bagian.

---

# 🔒 Password Hasher CLI

Tool sederhana berbasis **Command Line Interface (CLI)** untuk:

* Meng-hash password dengan berbagai algoritma (MD5, SHA, bcrypt, dll)
* Verifikasi password dengan hash (cocok untuk simulasi sistem login)

---

## ✨ Fitur

* Support beberapa algoritma: `md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `bcrypt`
* Pilih algoritma manual atau random
* Bisa verifikasi password terhadap hash (khusus bcrypt pakai `checkpw`)
* Simple dan ringan

---

## ⚡ Instalasi

```bash
git clone https://github.com/username/password-hasher-cli.git
cd password-hasher-cli
pip install bcrypt
```

---

## 🛠️ Cara Pakai

### 1. Hash password

```bash
# Default (sha256)
python3 hasher.py "mypassword"

# Pilih algoritma tertentu
python3 hasher.py "mypassword" -a md5
python3 hasher.py "mypassword" -a bcrypt

# Random algoritma
python3 hasher.py "mypassword" -r
```

### 2. Verifikasi password dengan hash

```bash
python3 hasher.py "mypassword" -a bcrypt -v '$2b$12$0WBNtSTuLzfgZ1tpRjkI9ehXleMGIGUEX2Rn3Nj7OduCjYrwLZdyq'
```

Output:

```
🔑 Password : mypassword
⚡ Algoritma: bcrypt
✅ Match    : True
```

---

## 📦 Contoh Output

Hash:

```
🔑 Password : mypassword
⚡ Algoritma: sha256
🔒 Hash     : 89e01536ac207279409d4de1e5253e01f4a1769e696db0d6062ca9b8f56767c8
```

Verifikasi:

```
🔑 Password : mypassword
⚡ Algoritma: bcrypt
✅ Match    : True
```

---

## 📌 Catatan

* Untuk simulasi keamanan beneran, gunakan **bcrypt** (lebih aman daripada MD5/SHA).
* Tool ini hanya untuk edukasi & latihan, jangan dipakai untuk sistem produksi serius tanpa tambahan keamanan.

---

## 🧑‍💻 License

MIT License

---

