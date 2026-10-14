class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        d, m = divmod(sum, 9)
        return f"{'9' * d}{m}{'0' * num}"[:num]


tests = [
    (2, 3, "30"),
    (2, 17, "98"),
    (1, 10, ""),
    (1, 1, "1"),
    (2, 18, "99"),
]

sol = Solution()
for a, b, out in tests:
    print(sol.maxSumOfSquares(a, b) == out)
