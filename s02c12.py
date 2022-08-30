import base64
import string
from s02c11 import random_key, detect_ecb
from s01c07 import encrypt_aes_ecb
from s02c09 import my_pad


def oracle(your_string: bytes) -> bytes:
    plain_text = my_pad(your_string + UNKNOWN_STRING)
    return encrypt_aes_ecb(KEY, plain_text)


def detect_block_size() -> int:
    i = 1
    inp = b'A' * i
    initial_len = len(oracle(inp))
    new_len = initial_len

    while new_len == initial_len:
        inp = b'A' * i
        i += 1
        new_len = len(oracle(inp))

    return new_len - initial_len


def decrypt_dict(attack_padding: bytes, decrypted_so_far: bytes, progress: int) -> bytes:
    expected_cipher_text = oracle(attack_padding)[:len(attack_padding)+progress+1]
    for c in string.printable:
        my_inp = attack_padding + decrypted_so_far + bytes(c, 'ascii')
        if oracle(my_inp)[:len(attack_padding)+progress+1] == expected_cipher_text:
            return bytes(c, 'ascii')

    return b''


def decryption_attack(block_size: int) -> bytes:
    plain_text = b''
    leng = len(oracle(b''))

    for i in range(leng):
        attack_padding = b'A' * (block_size - (1 + i) % block_size)
        plain_text += decrypt_dict(attack_padding, plain_text, i)

    return plain_text


if __name__ == "__main__":
    UNKNOWN_STRING = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGF'
                                      'pciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IH'
                                      'RvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    KEY = random_key()

    block_size = detect_block_size()
    is_ecb = detect_ecb(b'A'*100 + UNKNOWN_STRING, block_size)

    if is_ecb:
        print(bytes.decode(decryption_attack(block_size)))
    else:
        print('Not ECB, attack won\'t work')
