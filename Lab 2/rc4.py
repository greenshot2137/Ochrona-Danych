import math, time, itertools, sys
from collections import Counter


def rc4(key: bytes, data: bytes) -> bytes:
    # KSA
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i] 
    i = j = 0
    out = bytearray()
    for b in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  
        wynik = b ^ S[(S[i] + S[j]) % 256]
        out.append(wynik)

    return bytes(out)


def get_entropy(data: bytes) -> float:
    return -sum((c / len(data)) * math.log2(c / len(data)) for c in Counter(data).values())

assert rc4(b"abc", rc4(b"abc", b"test")) == b"test"

input_file = sys.argv[1]
with open(input_file, "rb") as f:
    cipher = f.read()

alphabet = [ord(c) for c in "abcdefghijklmnopqrstuvwxyz"]
candidates = []

start = time.perf_counter()
for p in itertools.product(alphabet, repeat=3):
    key = bytes(p)
    ent = get_entropy(rc4(key, cipher[:512]))  
    candidates.append((key, ent))
elapsed = time.perf_counter() - start

candidates.sort(key=lambda x: (x[1], x[0]))

print("Najlepsi kandydaci")
for key, ent in candidates[:5]:
    print(f"Klucz: {key.decode()} | Entropia: {ent:.4f}")

best_key = candidates[0][0]
plain = rc4(best_key, cipher)

with open("rc4.txt", "wb") as f:
    f.write(plain)

assert rc4(best_key, plain) == cipher

print(f"\nWybrany klucz: {best_key.decode()}")
print(f"Liczba prób: {len(candidates)} | Czas: {elapsed:.4f} s")
print(f"Entropia kryptogramu: {get_entropy(cipher):.4f}")
print(f"Entropia odszyfrowania: {get_entropy(plain):.4f}")