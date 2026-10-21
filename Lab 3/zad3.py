import math
from collections import Counter
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def get_entropy(data):
    if not data:
        return 0.0
    length = len(data)
    counts = Counter(data)
    return -sum((c / length) * math.log2(c / length) for c in counts.values())

with open("slaby_ecb.bin", "rb") as f:
    ciphertext = f.read()

sample = ciphertext[:4096]
charset = "abcdefghijklmnopqrstuvwxyz0123456789"
results = []
for char in charset:
    key = char.encode("ascii") * 16
    dec_sample = AES.new(key, AES.MODE_ECB).decrypt(sample)
    H = get_entropy(dec_sample)
    results.append((char, H))
results.sort(key=lambda x: x[1])

print("Najlepsi kandydaci")
for rank, (char, H) in enumerate(results[:5], 1):
    print(f"{rank}. Znak: {char} Entropia H: {H:.4f}")

best_char = results[0][0]
best_key = best_char.encode("ascii") * 16
full_dec_padded = AES.new(best_key, AES.MODE_ECB).decrypt(ciphertext)
full_decrypted = unpad(full_dec_padded, 16)

first_line = full_decrypted.decode("utf-8", errors="replace").splitlines()[0]
print(f"\nOdzyskany znak klucza: '{best_char}'")
print(f"Pierwszy wiersz tekstu: {first_line}")
