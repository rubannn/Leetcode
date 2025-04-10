class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        if len(nums) == len(set(nums)):
            return count
        for _ in range(n // 3):
            if len(nums) == len(set(nums)):
                return count
            nums = nums[3:]
            count += 1
        if len(nums) == len(set(nums)):
            return count
        if len(nums) > 0:
            count += 1
        return count
