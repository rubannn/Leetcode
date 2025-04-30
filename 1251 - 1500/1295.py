import math
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if num == 0:
                count = 1
            else:
                count = math.floor(math.log10(abs(num))) + 1
            if count % 2 == 0:
                res += 1
        return res
