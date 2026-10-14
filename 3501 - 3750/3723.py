class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        d, m = divmod(sum, 9)
        return f"{'9' * d}{m}{'0' * num}"[:num]
