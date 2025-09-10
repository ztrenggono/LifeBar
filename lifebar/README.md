# 🧬 Life Progress CLI

CLI sederhana buat ngeliat **progress hidup** dalam bentuk progress bar berwarna + emoji, plus dapet **quotes random** (bisa motivasi atau kocak).  
Inspirasi dari ide iseng: *"kalo hidup kita ada loading bar-nya, sekarang udah sampai mana ya?"* 😅

---

## 🚀 Fitur
- Hitung umur berdasarkan tahun lahir.
- Tampilkan progress bar hidup:
  - 🟩 Hijau = progress yang sudah ditempuh.
  - 🟥 Merah = sisa jalan yang belum ditempuh.
- Versi progress bar **emoji** (🟩 dan ⬜).
- Tampilkan estimasi tahun “game over” (umur target).
- Hitung sisa tahun hidup.
- Random quotes tiap kali dijalankan (campuran motivasi & kocak).

---

## 📦 Instalasi
Clone repo ini:
```bash
git clone https://github.com/username/life-progress-cli.git
cd life-progress-cli

Install dependency:

pip install colorama

Jalankan dengan Python (minimal versi 3.7+):

python3 life.py [tahun_lahir] [opsional: umur_target]

⚡ Contoh Penggunaan

python3 life.py 2009

Output contoh:

🎂 Umur kamu: 16 tahun
⏳ Progress hidup (warna): [██████------------------------] 20%
🎨 Progress hidup (emoji): 🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
📆 Target umur: 80 tahun (sekitar tahun 2089)
⌛ Sisa waktu hidup: 64 tahun

💡 Quote hari ini: Sukses itu 1% kerja keras, 99% drama keluarga. 🎭

Custom umur target:

python3 life.py 2009 100

Output contoh:

🎂 Umur kamu: 16 tahun
⏳ Progress hidup (warna): [█████-------------------------] 16%
🎨 Progress hidup (emoji): 🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
📆 Target umur: 100 tahun (sekitar tahun 2109)
⌛ Sisa waktu hidup: 84 tahun

💡 Quote hari ini: Hidup itu kayak WiFi, kadang kenceng kadang ngadat. 📶
