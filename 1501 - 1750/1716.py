class Solution:
    # variant 1
    def totalMoney(self, n: int) -> int:
        p, s = 1, 0
        while n > 7:
            s += (2 * p + 6) * 7 // 2
            n -= 7
            p += 1
        s += (2 * p + n - 1) * n // 2
        return s

    # variant 2
    def totalMoney2(self, n: int) -> int:
        res = 0
        a, b = divmod(n, 7)
        for i in range(1, a + 1):
            res += i + 3
        res = res * 7 + (2 * a + b + 1) * b // 2
        return res


sol = Solution()
tests = [
    (4, 10), (10, 37), (20, 96)
]

for n, ans in tests:
    print(sol.totalMoney(n) == ans)
