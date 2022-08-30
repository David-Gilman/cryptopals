def my_pad(text: bytes, block_size: int = 16) -> bytes:
    diff = -1 * len(text) % block_size
    padding = diff.to_bytes(1, 'big')
    return text + padding * diff


if __name__ == "__main__":
    print(my_pad(b"YELLOW SUBMARINE", 20))
