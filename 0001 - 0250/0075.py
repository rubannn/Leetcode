from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dc = Counter(nums)
        i = 0
        for x in (0, 1, 2):
            for _ in range(dc[x]):
                nums[i] = x
                i += 1
