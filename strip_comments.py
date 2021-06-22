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

    txt = [line.strip() + '\n' for line in result]
    result = ''.join(txt)
    if len(result) == 1:
        return result
    else:
        return result.strip()


print(strip("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
