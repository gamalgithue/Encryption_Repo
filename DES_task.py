from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(data.encode(), DES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return encrypted

def des_decrypt(key, encrypted_data):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded = cipher.decrypt(encrypted_data)
    decrypted = unpad(decrypted_padded, DES.block_size)
    return decrypted.decode()

# DES requires 8-byte key
key = b'8bytekey'  # 8 bytes = 64 bits

# Example usage
data = "HelloDES"
encrypted = des_encrypt(key, data)
decrypted = des_decrypt(key, encrypted)

print("Original:", data)
print("Encrypted (hex):", encrypted.hex())
print("Decrypted:", decrypted)
