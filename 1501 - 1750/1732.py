from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt, mx = 0, 0
        for x in gain:
            alt += x
            mx = max(mx, alt)
        return mx
