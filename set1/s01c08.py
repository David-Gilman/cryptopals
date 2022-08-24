import collections
from textwrap import wrap


def find_aes_cbc(file_name: str) -> str:
    with open(file_name, "r") as encrypted_file:
        for line in encrypted_file:
            wrapped_line = wrap(line, 16)

            for item, count in collections.Counter(wrapped_line).items():
                if count > 1:
                    return line


cbc_line = find_aes_cbc('8.txt')
print(cbc_line)
