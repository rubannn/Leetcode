class Solution:
    import math

    def hasGroupsSizeX(self, nums: List[int]) -> bool:
        dc = dict()
        for n in nums:
            if dc.get(n) is None:
                dc[n] = 1
            else:
                dc[n] += 1
        mn = min(dc.values())
        return math.gcd(*dc.values()) > 1
