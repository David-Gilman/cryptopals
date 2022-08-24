import base64
from s01c03 import xor_breaker
from s01c03 import score_text
from s01c05 import repeat_xor


def byte_hamming(str1, str2):
    count = 0
    for char_1, char_2 in zip(str1, str2):
        x = char_1 ^ char_2
        while x > 0:
            count += x & 1
            x >>= 1
    return count


def _key_finder(key_list: list[bytes], encrypted_data: bytes) -> (bytes, bytes):
    best_score = 0
    best_key = ''
    best_plaintext = ''
    for k_c in key_list:
        plain_text = repeat_xor(k_c, encrypted_data)
        curr_score = score_text(plain_text.decode("utf-8"))
        if curr_score > best_score:
            best_score = curr_score
            best_plaintext = plain_text
            best_key = k_c
    return best_key, best_plaintext


def vigenere_breaker(cipher_text):
    distances = {}
    for key_size in range(2, 41):
        avg = 0
        i = 0
        while i * key_size < len(cipher_text):
            first = cipher_text[i:i + key_size]
            second = cipher_text[i + key_size:i + key_size * 2]
            avg += byte_hamming(first, second) / key_size
            i += 1
        avg /= i
        distances[key_size] = avg

    possible_distances = sorted(distances, key=distances.get)[:3]
    keys = ['' for _ in range(3)]
    k = 0
    for key_size in possible_distances:
        i = 0
        blocks = [[] for _ in range(key_size)]
        while i < len(cipher_text):
            j = 0
            while j < key_size and i < len(cipher_text):
                blocks[j].append(cipher_text[i])
                j += 1
                i += 1
        for block in blocks:
            a = xor_breaker(bytes(block))
            keys[k] += chr(a['key'])
        k += 1

    return [bytes(c, 'utf-8') for c in keys]


assert byte_hamming(b'this is a test', b'wokka wokka!!!') == 37

file = open("6.txt", "r")
data = base64.b64decode(file.read())
key_candidates = vigenere_breaker(data)
f_key, final_plain_text = _key_finder(key_candidates, data)

print(f_key.decode('utf-8') + '\n')
print(final_plain_text.decode('utf-8'))
