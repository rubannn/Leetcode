def numTilings(n: int) -> int:
    dp = [1, 1, 2]
    if n < 3:
        return dp[n]
    for i in range(3, n + 1):
        dp.append(2 * dp[i-1] + dp[i-3])
    return dp[-1]


tests = [[3, 5], [1, 1], [4, 11], [5, 24], [6, 53], [7, 117]]

for n, ans in tests:
    print(numTilings(n) == ans)
