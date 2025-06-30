from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            j = i + 1
            while j < n and nums[j] - nums[i] <= 1:
                if nums[j] - nums[i] == 1:
                    res = max(res, j - i + 1)
                j += 1
        return res
