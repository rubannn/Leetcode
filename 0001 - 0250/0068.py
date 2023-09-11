def fullJustify(words: list, maxWidth: int) -> list:
    len_line = 0
    line = []
    result = []
    while words:
        if len_line + len(words[0]) <= maxWidth:
            len_line += len(words[0]) + 1
            line.append(words[0])
        else:
            result.append(line)
            len_line = len(words[0]) + 1
            line = [words[0]]
        words = words[1:]
    if line:
        result.append(line)

    for i, line in enumerate(result):
        count = len(line) - 1
        spaces = maxWidth - sum(len(w) for w in line)
        if count == 0:
            t = line[0] + " " * spaces
        elif i == len(result) - 1:
            sp = 1
            rest = spaces - count
            t = f'{" " * sp}'.join(line) + " " * rest
        elif count == 1:
            t = f'{" " * spaces}'.join(line)
        else:
            while spaces:
                for j in range(len(line) - 1):
                    line[j] = line[j] + ' '
                    spaces -= 1
                    if not spaces:
                        break
            t = ''.join(line)
        result[i] = t
    return result
