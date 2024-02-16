from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dc = sorted(Counter(arr).values())[::-1]
        while k > 0:
            x = dc[-1]
            if x > k:
                k = 0
            else:
                k -= x
                dc.pop()
        return len(dc)
