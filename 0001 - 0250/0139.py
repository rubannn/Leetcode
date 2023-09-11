def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    n = len(s) + 1
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = 1
    return dp[-1] == 1
