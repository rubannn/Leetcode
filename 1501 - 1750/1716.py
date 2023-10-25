class Solution:
    def totalMoney(self, n: int) -> int:
        p, s = 1, 0
        while n > 7:
            s += (2 * p + 6) * 7 // 2
            n -= 7
            p += 1
        s += (2 * p + n - 1) * n // 2
        return s
