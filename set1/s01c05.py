def repeat_xor(key, clear_text):
    cipher_text = b""
    clear_text = clear_text.strip()
    i = 0
    while i < len(clear_text):
        j = 0
        while j < len(key) and i < len(clear_text):
            cipher_text += bytes([ord(key[j]) ^ ord(clear_text[i])])
            i += 1
            j += 1
    return cipher_text.hex()


#text_file = "s01c05cleartext.txt"
text_file = "test.txt"
file = open(text_file, "r")
data = file.read()
print(repeat_xor("HACKER", data))
#print(repeat_xor("ICE", data))