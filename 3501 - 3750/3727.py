class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted([abs(x) for x in nums], reverse=True)
        a, b = 0, len(nums) - 1
        s = 0
        while a < b:
            s += nums[a] ** 2 - nums[b] ** 2
            a += 1
            b -= 1
        return s + (a == b) * nums[a] ** 2
