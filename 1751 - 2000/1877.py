class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[i] + nums[n-i-1] for i in range(n//2))
