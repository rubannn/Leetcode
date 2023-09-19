class Solution:
    # variant 1
    def isMonotonic(self, nums: List[int]) -> bool:
        a = b = True
        for i in range(len(nums) - 1):
            a = a and (nums[i] <= nums[i+1])
            b = b and (nums[i] >= nums[i+1])
        return a or b

    # variant 2
    def isMonotonic2(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums[::-1] == sorted(nums)
