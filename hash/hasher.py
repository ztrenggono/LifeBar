# file: hasher.py
import hashlib
import argparse
import random
import bcrypt

# List algoritma hash yang didukung hashlib
ALGORITHMS = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "bcrypt"]

def hash_password(password: str, algo: str):
    algo = algo.lower()
    if algo not in ALGORITHMS:
        raise ValueError(f"Algoritma '{algo}' gak didukung. Pilih dari: {', '.join(ALGORITHMS)}")

    if algo == "bcrypt":
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')
    else:
        h = hashlib.new(algo)
        h.update(password.encode('utf-8'))
        return h.hexdigest()

def verify_password(password: str, hashed: str, algo: str):
    algo = algo.lower()
    if algo == "bcrypt":
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    else:
        h = hashlib.new(algo)
        h.update(password.encode('utf-8'))
        return h.hexdigest() == hashed

def main():
    parser = argparse.ArgumentParser(description="Simple Password Hasher & Verifier CLI")
    parser.add_argument("password", help="Password yang mau di-hash / verify")
    parser.add_argument("-a", "--algo", help="Algoritma hash (default: sha256)", default="sha256")
    parser.add_argument("-r", "--random", action="store_true", help="Pilih algoritma random")
    parser.add_argument("-v", "--verify", help="Hash yang mau diverifikasi", default=None)

    args = parser.parse_args()

    algo = args.algo
    if args.random:
        algo = random.choice(ALGORITHMS)

    if args.verify:
        # Mode verifikasi
        match = verify_password(args.password, args.verify, algo)
        print(f"🔑 Password : {args.password}")
        print(f"⚡ Algoritma: {algo}")
        print(f"✅ Match    : {match}")
    else:
        # Mode hash
        hashed = hash_password(args.password, algo)
        print(f"🔑 Password : {args.password}")
        print(f"⚡ Algoritma: {algo}")
        print(f"🔒 Hash     : {hashed}")

if __name__ == "__main__":
    main()
