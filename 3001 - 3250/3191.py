class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        for i in range(n - 2):
            if nums[i]:
                continue
            nums[i] = not nums[i]
            nums[i + 1] = not nums[i + 1]
            nums[i + 2] = not nums[i + 2]
            k += 1
        return [-1, k][all(nums[-3:])]
