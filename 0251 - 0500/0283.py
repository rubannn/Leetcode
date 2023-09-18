class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = 0
        for n in nums:
            if n != 0:
                nums[x] = n
                x += 1
        nums[x:] = [0] * (len(nums) - x)
