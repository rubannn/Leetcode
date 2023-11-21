from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pairs = dict()
        for i, x in enumerate(nums):
            t = x - i
            pairs[t] = pairs.get(t, 0) + 1
        ans = 0
        for v in pairs.values():
            ans += v * (v - 1) // 2
        return len(nums) * (len(nums) - 1) // 2 - ans
