def rgb(hex_code: str):
    hex_code = separate_hex(hex_code)
    result = {
        'r': 0,
        'g': 0,
        'b': 0,
    }

    for i, color in enumerate(result):
        result[color] = int(hex_code[i], 16)

    return result


def separate_hex(hex_code):
    """This splits the hex code into a list of r, g, b"""
    hex_code = hex_code.replace('#', '')
    hex_c = []

    for i in range(3):
        hex_c.append(hex_code[:2])
        hex_code = hex_code[2:]

    return hex_c
