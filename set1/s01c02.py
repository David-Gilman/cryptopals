def str_xor(s1: hex, s2: hex) -> hex:
    s1_b = bytes.fromhex(s1)
    s2_b = bytes.fromhex(s2)
    b = b""
    for c1, c2 in zip(s1_b, s2_b):
        b += bytes([c1 ^ c2])
    return b.hex()

assert str_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") == "746865206b696420646f6e277420706c6179"
