class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: -abs(x))
        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] == 0:
                return abs(nums[i])
        return -1
