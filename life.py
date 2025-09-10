import datetime
import sys

def life_progress(birth_year, expected_age=80):
    today = datetime.date.today()
    age = today.year - birth_year
    progress = int((age / expected_age) * 50)  # scale ke 50 bar
    bar = "█" * progress + "-" * (50 - progress)
    print(f"Umur kamu: {age} tahun")
    print(f"Progress hidup: [{bar}] {age/expected_age:.0%}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python life.py [tahun_lahir] [opsional: umur_target]")
    else:
        birth_year = int(sys.argv[1])
        expected_age = int(sys.argv[2]) if len(sys.argv) > 2 else 80
        life_progress(birth_year, expected_age)
