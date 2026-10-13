class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted([x ** 2 for x in nums], reverse=True)
        a, b = 0, len(nums) - 1
        s = 0
        while a < b:
            s += nums[a] - nums[b]
            a += 1
            b -= 1
        return s + (a == b) * nums[a]
