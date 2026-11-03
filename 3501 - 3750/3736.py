class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        return sum(abs(mx - x) for x in nums)
