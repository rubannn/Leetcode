def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    res = []
    while len(s) > 0:
        res.append(s[:numRows])
        s = s[numRows:]
        diag = s[:numRows - 2]
        diag = ' ' + diag + ' '*(numRows - len(diag)- 1)
        res.append(diag[::-1])
        s = s[numRows - 2:]

    zigzag = ''
    for r in range(numRows):
        for c in res:
            if r < len(c) and c[r] != ' ':
                zigzag += c[r]
    return zigzag


s = "PAYPALISHIRING"
numRows = 3
res = "PAHNAPLSIIGYIR"
print(convert(s, numRows) == res)


s = "PAYPALISHIRING"
numRows = 4
res = "PINALSIGYAHRPI"
print(convert(s, numRows) == res)


s = "ABC"
numRows = 2
res = "ACB"
print(convert(s, numRows) == res)

s = "ABC"
numRows = 1
res = "ABC"
print(convert(s, numRows) == res)


s = "ABCDE"
numRows = 4
res = "ABCED"
print(convert(s, numRows) == res)
