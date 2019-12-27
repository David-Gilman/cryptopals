from binascii import unhexlify


def strxor(s1, s2):
    bytes1 = unhexlify(s1)
    bytes2 = unhexlify(s2)
    b = b""
    for c1, c2 in zip(bytes1, bytes2):
        b += bytes([c1 ^ c2])
    return b.hex()


print(strxor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))
