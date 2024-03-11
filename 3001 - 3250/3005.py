from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dc = Counter(nums)
        mx = max(dc.values())
        dc_mx = Counter(dc.values())
        return dc_mx[mx] * mx
