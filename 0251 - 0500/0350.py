from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dc1 = Counter(nums1)
        dc2 = Counter(nums2)
        res = []
        for k in set(dc1.keys()) & set(dc2.keys()):
            res.extend([k] * min(dc1[k], dc2[k]))
        return res
