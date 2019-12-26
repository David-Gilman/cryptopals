from binascii import unhexlify


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
    cipher_text = unhexlify(inp)
    possible_clear_texts = {}
    for key in range(256):
        clear_text = ""
        for char in cipher_text:
            clear_text += chr(char ^ key)
        possible_clear_texts[clear_text] = score_text(clear_text)
    ans = max(possible_clear_texts, key=possible_clear_texts.get)
    return ans, possible_clear_texts[ans]


def cipher_parser(path):
    f = open(path, "r")
    lines = {}
    for line in f:
        line = line.strip()
        key, value = xor_breaker(line)
        lines[key] = value
    return max(lines, key=lines.get)


print(cipher_parser("ciphertext.txt"))
