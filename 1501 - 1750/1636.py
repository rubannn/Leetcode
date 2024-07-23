from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dc = Counter(nums)
        nums.sort(key=lambda x: (dc[x], -x))
        return nums
