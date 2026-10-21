import sys
def encrypt(p: bytes, k: bytes) -> bytes:
    return bytes([(p[i] + k[i % len(k)]) % 256 for i in range(len(p))])

def decrypt(c: bytes, k: bytes) -> bytes:
    return bytes([(c[i] - k[i % len(k)]) % 256 for i in range(len(c))])


input_file = sys.argv[1]
with open(input_file, "rb") as f:
    data = f.read()

key1 = b"ZAMEK"
cipher = encrypt(data, key1)

with open("vigenere.bin", "wb") as f:
    f.write(cipher)


plain = decrypt(cipher, key1)
print("Zgodność z oryginałem:", plain == data)


print("Puste dane:", decrypt(encrypt(b"", key1), key1) == b"")
print("Bajty 0 i 255:", decrypt(encrypt(bytes([0, 255]), key1), key1) == bytes([0, 255]))


txt = b"BRAMABRAMABRAMA"
c1 = encrypt(txt, b"SZYFR").hex()
c2 = encrypt(txt, b"KOD").hex()

print("SZYFR:", c1[:10], c1[10:20], c1[20:30])
print("KOD:  ", c2[:10], c2[10:20], c2[20:30])