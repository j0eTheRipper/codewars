def rgb(r, g, b):
    colors = [r, g, b]
    colors = validate_rgb(colors)
    colors = convert_to_hex(colors)

    result = validate_hex(colors)

    return result


def validate_hex(colors):
    result = ''

    for color in colors:
        if len(color) == 2:
            result += color
        else:
            result += f'0{color}'

    return result


def convert_to_hex(colors):
    for i, color in enumerate(colors):
        colors[i] = hex(color).replace('0x', '').upper()

    return colors


def validate_rgb(colors):
    for i, color in enumerate(colors):
        if color < 0:
            colors[i] = 0
        elif color > 255:
            colors[i] = 255

    return colors
