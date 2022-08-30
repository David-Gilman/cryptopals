from s01c03 import xor_breaker


def cipher_parser(path: str) -> str:
    f = open(path, "r")
    lines = {}
    for line in f:
        line = line.strip()
        a = xor_breaker(bytes.fromhex(line))
        lines[a['text']] = a['score']
    return max(lines, key=lines.get)


if __name__ == "__main__":
    assert cipher_parser("4.txt") == "Now that the party is jumping\n"
