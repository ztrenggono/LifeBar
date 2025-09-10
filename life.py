import datetime
import sys
import random
from colorama import Fore, Style, init

# init colorama
init(autoreset=True)

QUOTES = [
    # Motivasi
    "Hidup adalah perjuangan, jangan menyerah. 💪",
    "Setiap hari adalah kesempatan baru. 🌅",
    "Kegagalan hanyalah batu loncatan menuju sukses. 🚀",
    "Jangan tunggu waktu tepat, buat waktumu tepat. ⏳",
    "Percaya diri adalah kunci awal keberhasilan. 🔑",

    # Kocak
    "Hidup itu kayak WiFi, kadang kenceng kadang ngadat. 📶",
    "Mimpi setinggi langit, bangun tetep di kasur. 🛌",
    "Sukses itu 1% kerja keras, 99% drama keluarga. 🎭",
    "Kalau hidupmu berat, mungkin kamu kurang makan nasi. 🍚",
    "Jangan stres, nanti cepat tua. Tapi tua itu pasti sih. 👴"
]

def life_progress(birth_year, expected_age=80):
    today = datetime.date.today()
    age = today.year - birth_year

    if age < 0:
        print("⚠️ Tahun lahir tidak valid!")
        return

    # progress bar
    progress = int((age / expected_age) * 30)  # scale ke 30 bar
    filled = Fore.GREEN + "█" * progress
    empty = Fore.RED + "-" * (30 - progress)
    bar = filled + empty + Style.RESET_ALL

    # emoji progress bar
    emoji_bar = "🟩" * progress + "⬜" * (30 - progress)

    # info tambahan
    years_left = expected_age - age
    game_over_year = birth_year + expected_age

    # output
    print(f"🎂 Umur kamu: {age} tahun")
    print(f"⏳ Progress hidup (warna): [{bar}] {age/expected_age:.0%}")
    print(f"🎨 Progress hidup (emoji): {emoji_bar}")
    print(f"📆 Target umur: {expected_age} tahun (sekitar tahun {game_over_year})")
    print(f"⌛ Sisa waktu hidup: {years_left} tahun")
    print()
    print("💡 Quote hari ini:", random.choice(QUOTES))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 life.py [tahun_lahir] [opsional: umur_target]")
    else:
        birth_year = int(sys.argv[1])
        expected_age = int(sys.argv[2]) if len(sys.argv) > 2 else 80
        life_progress(birth_year, expected_age)
