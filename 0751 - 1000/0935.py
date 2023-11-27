# https://oeis.org/A327692
class Solution:
    def knightDialer(self, n: int) -> int:
        reach = ((4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4))
        dp = [[0] * 10 for _ in range(n)]
        dp[0] = [1]*10
        for step in range(1, n):
            for btn in range(10):
                for nxt in reach[btn]:
                    dp[step][nxt] += dp[step-1][btn]
        return [sum(row) for row in dp][-1] % (10**9 + 7)
