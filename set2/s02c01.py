def pad(text: str, block_size: int) -> str:
    return text + '\x04' * (block_size % len(text))


def main():
    inp = "YELLOW SUBMARINE"
    string = pad(inp, 20)
    for character in string:
        print(character.encode('utf-8').hex(), end='')


if __name__ == '__main__':
    main()
