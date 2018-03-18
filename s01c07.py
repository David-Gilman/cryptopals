from Crypto.Cipher import AES
import base64


key = b"YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)
text_file = "7.txt"
encrypted_file = open(text_file, "r").read()
encrypted_data = base64.b64decode(encrypted_file)
clear_data = cipher.decrypt(encrypted_data)
print(clear_data)
