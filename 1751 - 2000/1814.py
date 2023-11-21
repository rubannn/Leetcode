from typing import List

class Solution:
    # variant 1 (8145 ms; 26.8 MB)
    def countNicePairs(self, nums: List[int]) -> int:
        mmod = 1000000007
        sups = [x - int(str(x)[::-1]) for x in nums]
        pairs = {el: sups.count(el) for el in set(sups)}
        ans = 0
        for v in pairs.values():
            if v > 1:
                ans = (ans + v * (v - 1) // 2) % mmod
        return ans

    # variant 2 (555 ms; 26.9 MB)
    def countNicePairs(self, nums: List[int]) -> int:
        mmod = 1000000007
        pairs = dict()
        for x in nums:
            t = x - int(str(x)[::-1])
            pairs[t] = pairs.get(t, 0) + 1
        ans = 0
        for v in pairs.values():
            if v > 1:
                ans = (ans + v * (v - 1) // 2) % mmod
        return ans
