from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dc = Counter(nums)
        return all(x % 2 == 0 for x in dc.values())
