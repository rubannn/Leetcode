class Solution:
    # variant 1
    def numberOfMatches(self, n: int) -> int:
        m = 0
        while n > 1:
            m += n // 2
            n = n // 2 + n % 2
        return m

    # variant 2
    def numberOfMatches2(self, n: int) -> int:
        return n - 1
