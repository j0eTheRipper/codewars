def strip(txt: str, markers: list):
    txt = txt.split('\n')
    result = []

    for line in txt:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0]
                result.append(line)
                break
        else:
            result.append(line)

    txt = ''.join([line.strip() + '\n' for line in result])

    if validate(txt, markers):
        return strip(txt, markers)
    else:
        return txt.strip()


def validate(txt: str, markers: list):
    for marker in markers:
        if marker in txt:
            return True
    else:
        return False
