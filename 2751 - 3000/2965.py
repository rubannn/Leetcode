from typing import List
from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        dc = Counter([item for row in grid for item in row])
        missing = (set(range(1, n * n + 1)) - set(dc.keys())).pop()
        return [max(dc, key=dc.get), missing]


tests = [([[1, 3], [2, 2]], [2, 4]), ([[9, 1, 7], [8, 9, 2], [3, 4, 6]], [9, 5])]
sol = Solution()
for t, ans in tests:
    print(sol.findMissingAndRepeatedValues(t) == ans)
