class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        m = 10**9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for cubik in range(1, n + 1):
            for total in range(cubik, target + 1):
                dp[cubik][total] = sum(dp[cubik - 1][max(total - k, 0) : total]) % m
        return dp[-1][-1]
