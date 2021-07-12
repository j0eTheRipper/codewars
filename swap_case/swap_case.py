from collections import defaultdict


def swap(string: str, n: int):
    binary_n = bin(n).replace('0b', '')
    string, indices = strip_punctuation(string)

    if len(binary_n) >= len(string):
        return main(string, binary_n)
    else:
        letters_needed = len(string) // len(binary_n)

        if letters_needed * len(binary_n) >= len(string):
            binary_n = binary_n * letters_needed
            string = main(string, binary_n)
            return return_punctuation(string, indices)
        else:
            binary_n = binary_n * (letters_needed + 1)
            string = main(string, binary_n)
            return return_punctuation(string, indices)


def main(string: str, binary_n: str):
    for i, char in enumerate(string):
        if binary_n[i] == '1':
            string = string.replace(char, char.swapcase())

    return string


def strip_punctuation(string: str):
    indices = defaultdict(list)
    output_string = ''

    for i, char in enumerate(string):
        if not char.isalpha():
            indices[char].append(i)
        else:
            output_string += char

    return output_string, dict(indices)


def return_punctuation(string: str, indices: dict):
    string = list(string)
    for char, index_list in indices.items():
        for i in index_list:
            string.insert(i, char)

    return ''.join(string)


if __name__ == '__main__':
    print(strip_punctuation('Hello world!'))
