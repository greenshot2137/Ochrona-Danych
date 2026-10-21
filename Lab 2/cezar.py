import sys
input_file = sys.argv[1]
with open(input_file, "rb") as f:
    data = f.read()


candidates = []
for k in range(256):
    dec = bytes([(b - k) % 256 for b in data])
    score = sum(1 for b in dec if 32 <= b <= 126 or b in (9, 10, 13)) / len(dec)
    candidates.append((k, score, dec))


candidates.sort(key=lambda x: (-x[1], x[0]))

print("Najlepsi kandydaci")
for k, score, dec in candidates[:5]:
        print(f"k = {k:3d} | Ocena: {score:.4f} | Tekst: {repr(dec[:50])}")

  
    

    #po uruchomieniu programu wybieram najlepszego kandydata recznie
best = None
for k, score, decrypted in candidates:
    if k == 233:
        best = decrypted
        break 


with open("cezar.txt", "wb") as f:
        f.write(best)



