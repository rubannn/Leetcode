class Solution:
    def numberOfCuts(self, n: int) -> int:
        return (n // 2, n, 0)[2 if n == 1 else n % 2]
