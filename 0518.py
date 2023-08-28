def change(self, amount: int, coins: list[int]) -> int:
    dn = [0] * (amount + 1)
    dn[0] = 1
    for c in coins:
        for x in range(c, amount + 1):
            dn[x] += dn[x - c]
    return dn[-1]
