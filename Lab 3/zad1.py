import os
from Crypto.Cipher import AES

data = b"0123456789ABCDEF" * 4
key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
iv = os.urandom(16)

cipher_ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = cipher_ecb.encrypt(data)
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
ct_cbc = cipher_cbc.encrypt(data)


print("Bloki ECB")
for i in range(0, len(ct_ecb), 16):
    print(f"Blok {i//16 + 1}: {ct_ecb[i:i+16].hex()}")
print("\nBloki CBC")
for i in range(0, len(ct_cbc), 16):
    print(f"Blok {i//16 + 1}: {ct_cbc[i:i+16].hex()}")

pt_ecb = AES.new(key, AES.MODE_ECB).decrypt(ct_ecb)
pt_cbc = AES.new(key, AES.MODE_CBC, iv).decrypt(ct_cbc)

print(f"\nOdszyfrowanie ECB {pt_ecb == data}")
print(f"Odszyfrowanie CBC: {pt_cbc == data}")