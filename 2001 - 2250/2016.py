from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        mn = nums[0]

        for j in range(1, len(nums)):
            if nums[j] > mn:
                diff = nums[j] - mn
                if diff > max_diff:
                    max_diff = diff
            else:
                mn = nums[j]
        return max_diff
