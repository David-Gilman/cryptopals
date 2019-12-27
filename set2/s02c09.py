def my_pad(text: bytes, block_size: int) -> bytes:
    text_bytes = bytearray(text)
    for i in range(block_size % len(text_bytes)):
        text_bytes.append(4)
    return bytes(text_bytes)


def main():
    print(my_pad(b"YELLOW SUBMARINE", 20))


if __name__ == '__main__':
    main()
