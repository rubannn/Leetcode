import heapq
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for _ in range(k):
            mx = -nums[0]
            res += mx
            heapq.heapreplace(nums, -ceil(mx / 3))
        return res
