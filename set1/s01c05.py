def repeat_xor(key: bytes, text: bytes) -> bytes:
    out_text = b""
    text = text.strip()
    i = 0
    while i < len(text):
        j = 0
        while j < len(key) and i < len(text):
            out_text += bytes([key[j] ^ text[i]])
            i += 1
            j += 1
    return out_text


plain_text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272" \
           "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
assert repeat_xor(b'ICE', plain_text).hex() == expected
