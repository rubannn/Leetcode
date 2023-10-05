from math import floor
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dct = Counter(nums)
        t = floor(len(nums) / 3)
        return [x for x, y in dct.items() if y > t]
