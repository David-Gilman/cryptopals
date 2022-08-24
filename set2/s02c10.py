from Crypto.Cipher import AES
import base64
from binascii import unhexlify

"""
WIP"""


def str_xor(s1: str, s2: str) -> str:
    # bytes1 = unhexlify(s1)
    # bytes2 = unhexlify(s2)
    print(s1)
    print(s2)
    b = b""
    for c1, c2 in zip(s1, s2):
        b += bytes([ord(c1) ^ ord(c2)])
    print(len(b))
    return b#.hex()


def ecb_decrypt(key: bytes, cipher_text: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = base64.b64decode(cipher_text)
    return cipher.decrypt(encrypted_data)


def ecb_encrypt(key: bytes, plain_text: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = my_pad(plain_text, 16)
    encrypted_text = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted_text)


def my_pad(text: bytes, block_size: int) -> bytes:
    text_bytes = bytearray(text)
    for i in range(block_size % len(text_bytes)):
        text_bytes.append(4)
    return bytes(text_bytes)


def cbc_encrypt(key: bytes, iv: bytes, plain_text: bytes) -> bytes:
    plain_text = my_pad(plain_text, 16)
    previous_block = str(iv)
    cipher_text = b""
    i = 0
    while i < len(plain_text):
        current_block = base64.encodebytes(plain_text[i: i + 16])
        current_block = str_xor(previous_block, str(current_block))
        encrypted_block = ecb_encrypt(key, current_block)
        cipher_text += encrypted_block
        previous_block = encrypted_block
        i += 16

    return cipher_text


def main():
    # cipher_text = ecb_encrypt(b"YELLOW_SUBMARINE", b"1234567890ABC")
    # print(ecb_decrypt(b"YELLOW_SUBMARINE", cipher_text))
    cipher_text = cbc_encrypt(bytes("YELLOW_SUBMARINE", 'utf-8'), bytes.fromhex("00") * 16, bytes("1234567890ABC", 'utf-8'))
    print(cipher_text)


if __name__ == '__main__':
    main()
