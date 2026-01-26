class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        mn = nums[k - 1] - nums[0]
        for i in range(len(nums) - k + 1):
            mn = min(mn, nums[i + k - 1] - nums[i])
        return mn
