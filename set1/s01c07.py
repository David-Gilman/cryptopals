from Crypto.Cipher import AES
import base64


def main():
    key = b"YELLOW SUBMARINE"
    cipher = AES.new(key, AES.MODE_ECB)
    text_file = "S01C07input.txt"
    encrypted_file = open(text_file, "r").read()
    encrypted_data = base64.b64decode(encrypted_file)
    clear_data = cipher.decrypt(encrypted_data)
    print(clear_data.decode("utf-8"))


if __name__ == '__main__':
    main()
