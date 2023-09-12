class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        for x in range(5, n+1, 5):
            while x % 5 == 0:
                res += 1
                x //= 5
        return res
