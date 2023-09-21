class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            nums = [(max, min)[i % 4 == 0](nums[i], nums[i+1]) for i in range(0, n, 2)]
            n = len(nums)
        return nums[0]
