ENGLISH_FREQS = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


def score_text(inp: str) -> int:
    score = 0
    for char in inp:
        score += ENGLISH_FREQS.get(char.lower(), 0)
    return score


def xor_breaker(inp: bytes) -> dict:
    possible_clear_texts = []
    for key in range(255):
        clear_text = ""
        for char in inp:
            clear_text += chr(char ^ key)
        possible_clear_texts.append({'text': clear_text, 'score': score_text(clear_text), 'key': key})
    return sorted(possible_clear_texts, key=lambda cand: cand['score'], reverse=True)[0]


a = xor_breaker(bytes.fromhex(
    "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
assert a['text'] == "Cooking MC's like a pound of bacon"
