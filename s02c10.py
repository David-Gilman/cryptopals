import base64

from s01c07 import decrypt_aes_ecb, encrypt_aes_ecb
from s02c09 import my_pad


def xor(inp1: bytes, inp2: bytes) -> bytes:
    b = b''
    for c1, c2 in zip(inp1, inp2):
        b += bytes([c1 ^ c2])
    return b


def cbc_encrypt(key: bytes, iv: bytes, plain_text: bytes) -> bytes:
    plain_text = my_pad(plain_text, 16)
    previous_block = iv
    cipher_text = b''

    for i in range(0, len(plain_text), 16):
        current_block = xor(previous_block, plain_text[i: i + 16])
        encrypted_block = encrypt_aes_ecb(key, current_block)
        cipher_text += encrypted_block
        previous_block = encrypted_block

    return cipher_text


def cbc_decrypt(key: bytes, iv: bytes, cipher_text: bytes) -> bytes:
    plain_text = b''
    previous_block = iv

    for i in range(0, len(cipher_text), 16):
        current_block = cipher_text[i: i + 16]
        plain_text_block = decrypt_aes_ecb(key, current_block)
        plain_text += xor(plain_text_block, previous_block)
        previous_block = current_block

    return plain_text


if __name__ == "__main__":
    secret_key = b"YELLOW_SUBMARINE"
    this_iv = bytes.fromhex("00") * 16
    og_text = bytes("A" * 16, 'utf-8')

    a = cbc_encrypt(secret_key, this_iv, og_text)
    b = cbc_decrypt(secret_key, this_iv, a)
    assert b == bytes("A" * 16, 'utf-8')

    encrypted_file = open("10.txt", "r").read()
    encrypted_data = base64.b64decode(encrypted_file)
    final = cbc_decrypt(b"YELLOW SUBMARINE", this_iv, encrypted_data)
    print(final.decode("utf-8"))
