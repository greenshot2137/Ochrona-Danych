import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

def cipher_pass(password, data):
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = PBKDF2(password, salt, dkLen=32, count=200000, hmac_hash_module=SHA256)
    padded_data = pad(data, 16)
    ct = AES.new(key, AES.MODE_CBC, iv).encrypt(padded_data)
    padded_dec = AES.new(key, AES.MODE_CBC, iv).decrypt(ct)
    decrypted = unpad(padded_dec, 16)

    return ct, decrypted

password = b"KochamPolitechnnikeWarszawska"

with open("wiadomosc.txt", "rb") as f:
    file_bytes = f.read()
    
tests = [
    ("Puste dane", b""),
    ("16B ASCII", b"0123456789ABCDEF"),
    ("wiadomosc.txt", file_bytes)
]

for name, input_bytes in tests:
    ct, dec = cipher_pass(password, input_bytes)
    print(f"Wejscie: {name} Rozmiar: {len(input_bytes)}B Kryptogram: {len(ct)}B     Zgodność: {input_bytes == dec}")

ct1, _ = cipher_pass(password, file_bytes)
ct2, _ = cipher_pass(password, file_bytes)
print(f"\nCzy szyfrowania tej samej wiadomosci sa takie same? {ct1 == ct2}")
