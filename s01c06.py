import base64


def repeat_xor(key, text):
    out_text = b""
    text = text.strip()
    i = 0
    while i < len(text):
        j = 0
        while j < len(key) and i < len(text):
            out_text += bytes([ord(key[j]) ^ text[i]])
            i += 1
            j += 1
    return out_text.decode('utf-8')


def score_text(inp):
    english_freqs = {
        'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
        'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
        'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
        'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836
    }
    score = 0
    for char in inp:
        if char in english_freqs:
            score += english_freqs[char.lower()]
    return score


def xor_breaker(inp):
    possible_clear_texts = {}
    for k in range(256):
        clear_text = ""
        for char in inp:
            clear_text += chr(char ^ k)
        possible_clear_texts[k] = score_text(clear_text)
    ans = max(possible_clear_texts, key=possible_clear_texts.get)
    return ans


def byte_hamming(str1, str2):
    count = 0
    for char_1, char_2 in zip(str1, str2):
        x = char_1 ^ char_2
        while x > 0:
            count += x & 1
            x >>= 1
    return count


def vigenere_breaker(cipher_text):
    distances = {}
    key_size = 2
    while key_size <= 40:
        avg = 0
        i = 0
        while i*key_size < len(cipher_text):
            first = cipher_text[i:i+key_size]
            second = cipher_text[i+key_size:i+key_size*2]
            avg += byte_hamming(first, second) / key_size
            i += 1
        avg /= i
        distances[key_size] = avg
        key_size += 1

    possible_distances = sorted(distances, key=distances.get)[:3]
    keys = [[] for _ in range(3)]
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
            keys[k].append(chr(xor_breaker(block)))
        k += 1
    return keys[0]


text_file = "6.txt"
file = open(text_file, "r")
data = base64.b64decode(file.read())
print(repeat_xor(vigenere_breaker(data), data))