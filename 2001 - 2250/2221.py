class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for p in range(n - 1):
            for i in range(n - p - 1):
                nums[i] = (nums[i] + nums[i+1]) % 10
        return nums[0]
