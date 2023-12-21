from collections import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        pq = []
        heapq.heapify(pq)
        cur_sum = 0
        cur_res = 0
        for a, b in pairs:
            cur_sum = cur_sum + b
            heapq.heappush(pq, b)
            if len(pq) == k:
                cur_res = max(cur_res, cur_sum * a)
                cur_sum -= heapq.heappop(pq)
        return cur_res
