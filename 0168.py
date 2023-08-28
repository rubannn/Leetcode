def convertToTitle(self, num: int) -> str:
    sol, p = '', ord('A')
    while num > 0:
        num -= 1
        sol = chr(num % 26 + p) + sol
        num //= 26
    return sol
