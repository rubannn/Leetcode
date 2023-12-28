class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                cnt, del_cnt = 0, 0

                for t in range(i, 0, -1):
                    if s[t - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        del_cnt += 1

                    if j >= del_cnt:
                        cost = 1 + (cnt >= 2) + (cnt >= 10) + (cnt >= 100)
                        dp[i][j] = min(dp[i][j], dp[t - 1][j - del_cnt] + cost)
        return dp[n][k]


tests = [
    ("aaabcccd", 2, 4),
    ("aabbaa", 2, 2),
    ("aaaaaaaaaaa", 0, 3),
    ("bababbaba", 1, 7),
    ("iaiaiaiaiaiaiaiaiaa", 1, 17),
    ("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk", 41, 2),
    ("x", 1, 0),
    ("eoongjjkjfelnkgkjohfjfjfhkmnmmlinkihhlfipgoejiniol", 13, 32),
]
sol = Solution()
for s, k, ans in tests:
    print(sol.getLengthOfOptimalCompression(s, k) == ans)
