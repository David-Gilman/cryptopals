"""import sys
import crypto
sys.modules['Crypto'] = crypto"""
from crypto.Cipher import AES
import base64


key = b"YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)
text_file = "7.txt"
file = open(text_file, "r")
data = base64.b64decode(cipher.decrypt(file.read()))