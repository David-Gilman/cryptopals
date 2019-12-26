import collections
from textwrap import wrap


def main():
    text_file = "S01C08input.txt"
    with open(text_file, "r") as encrypted_file:
        for line in encrypted_file:
            wrapped_line = wrap(line, 16)

            for item, count in collections.Counter(wrapped_line).items():
                if count > 1:
                    print(line)
                    break


if __name__ == '__main__':
    main()
