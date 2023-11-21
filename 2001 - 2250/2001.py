from typing import List

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        pairs = dict()
        for p in rectangles:
            t = p[0] / p[1]
            pairs[t] = pairs.get(t, 0) + 1
        ans = 0
        for v in pairs.values():
            if v > 1:
                ans += v * (v - 1) // 2
        return ans
