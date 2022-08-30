import random
from s02c10 import cbc_encrypt
from s01c07 import encrypt_aes_ecb
from s02c09 import my_pad


def random_key(key_length: int = 16) -> bytes:
    return random.randbytes(key_length)


def appended_random_bytes(inp: bytes) -> bytes:
    pre_length = random.randint(5, 10)
    post_length = random.randint(5, 10)
    return random.randbytes(pre_length) + inp + random.randbytes(post_length)


def encryption_oracle(inp: bytes) -> bytes:
    key = random_key()
    inp = appended_random_bytes(inp)

    if random.randint(0, 1) == 0:
        print('CBC')
        iv = random_key()
        return cbc_encrypt(key, iv, inp)
    else:
        print('ECB')
        inp = my_pad(inp, 16)
        return encrypt_aes_ecb(key, inp)


def detect_ecb(cipher_text: bytes, block_size: int = 16) -> bool:
    line_dict = set()
    for i in range(0, len(cipher_text), block_size):
        block = cipher_text[i: block_size+i]

        if block in line_dict:
            return True
        line_dict.add(block)

    return False


if __name__ == "__main__":
    attack_data = b'A' * 64
    encrypted = encryption_oracle(attack_data)
    if detect_ecb(encrypted):
        print('ECB')
    else:
        print('CBC')
