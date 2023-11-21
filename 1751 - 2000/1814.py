from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mmod = 1000000007
        sups = [x - int(str(x)[::-1]) for x in nums]
        pairs = {el: sups.count(el) for el in set(sups)}
        ans = 0
        for v in pairs.values():
            if v > 1:
                ans = (ans + v * (v - 1) // 2) % mmod
        return ans
