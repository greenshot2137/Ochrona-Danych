import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes



data = b"0123456789ABCDEF" * 4
key = bytes.fromhexA("000102030405060708090a0b0c0d0e0f")
iv = os.urandom(16)

cipher_ecb = Cipher(algorithms.AES(key), modes.ECB())
ct_ecb = cipher_ecb.encryptor().update(data)

cipher_cbc = Cipher(algorithms.AES(key), modes.CBC(iv))
ct_cbc = cipher_cbc.encryptor().update(data)


print("Bloki EBC")
for i in range(0, len(ct_ecb), 16):
    print(f"Blok {i//16 + 1}: {ct_ecb[i:i+16].hex()}")

print("\nBloki CBC")
for i in range(0, len(ct_cbc), 16):
    print(f"Blok {i//16 + 1}: {ct_cbc[i:i+16].hex()}")


pt_ecb = cipher_ecb.decryptor().update(ct_ecb)
pt_cbc = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor().update(ct_cbc)

print(f"\nOdszyfrowanie ECB: {pt_ecb == data}")
print(f"Odszyfrowanie CBC: {pt_cbc == data}")



