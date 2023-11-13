class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        d, s = len(nums), 0
        for i, n in enumerate(nums):
            if d % (i+1) == 0:
                s += n * n
        return s
