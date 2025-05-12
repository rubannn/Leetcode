from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1, s1 = nums1.count(0), sum(nums1)
        z2, s2 = nums2.count(0), sum(nums2)
        if (z1 == 0) and (s1 < s2 + z2) or (z2 == 0) and (s1 + z1 > s2):
            return -1
        return max(s1 + z1, s2 + z2)
