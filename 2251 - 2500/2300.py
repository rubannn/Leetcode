from typing import List
from bisect import bisect_left


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for s in spells:
            t = success / s
            ans.append(n - bisect_left(potions, t))
        return ans
