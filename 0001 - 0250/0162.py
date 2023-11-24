class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        p = 0
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1] and nums[i] > nums[p]:
                p = i
        if nums[-1] > nums[p]:
            p = len(nums)-1
        return p
