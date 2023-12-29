from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1

        dp = [[float("inf")] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(d + 1, i + 1)):
                mx = -1
                for p in range(i, 0, -1):
                    mx = max(mx, jobDifficulty[p - 1])
                    dp[i][j] = min(dp[i][j], dp[p - 1][j - 1] + mx)
        return (dp[n][d], -1)[dp[n][d] >= float("inf")]


tests = [
    ([6, 5, 4, 3, 2, 1], 2, 7),
    ([9, 9, 9], 4, -1),
    ([1, 1, 1], 3, 3),
    ([3, 4, 6, 1, 5, 8, 3, 8, 2, 4], 3, 14),  # (3, 4, 6, 1, 5, 8, 3, 8,) (2,) (4)
    ([5, 1, 6, 3, 1, 1], 4, 11),
    ([1, 1, 1, 5, 6], 3, 8),
    ([7, 1, 7, 1, 7, 1], 3, 15),  # (7, 1, 7, 1,) (7,) (1)
    ([34, 12, 9, 6, 0, 1], 2, 35),
    (
        [186, 398, 479, 206, 885, 423, 805, 112, 925, 656, 16, 932, 740, 292, 671, 360],
        4,
        1803,
    ),  # (186,) (398, 479,) (206,) (885, 423, 805, 112, 925, 656, 16, 932, 740, 292, 671, 360)
]
sol = Solution()
for jobs, d, ans in tests:
    print(sol.minDifficulty(jobs, d) == ans)
