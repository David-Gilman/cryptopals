from Crypto.Cipher import AES
import base64


def decrypt_aes_ecb(key: bytes, cipher_text: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(cipher_text)


encrypted_file = open("7.txt", "r").read()
encrypted_data = base64.b64decode(encrypted_file)
final = decrypt_aes_ecb(b"YELLOW SUBMARINE", encrypted_data)
print(final.decode("utf-8"))
