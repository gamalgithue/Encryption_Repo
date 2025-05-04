from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    iv = cipher.iv
    return iv + ct_bytes

def decrypt(cipher_text, key):
    iv = cipher_text[:AES.block_size]
    ct = cipher_text[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

key = os.urandom(16)
plain_text = "Mostafa Badr"
encrypted = encrypt(plain_text, key)
print("Encrypted:", encrypted)
decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)