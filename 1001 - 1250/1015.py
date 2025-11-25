class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1 % k
        for x in range(1, k + 1):
            if n == 0:
                return x
            n = (n * 10 + 1) % k
        return -1
