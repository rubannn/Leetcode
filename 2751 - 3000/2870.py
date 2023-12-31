from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for v in Counter(nums).values():
            if v == 1:
                return -1
            else:
                res += (v + 2) // 3
        return res


tests = [
    ([2, 3, 3, 2, 2, 4, 2, 3, 4], 4),
    ([2, 1, 2, 2, 3, 3], -1),
    ([14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12], 7),
    ([19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19], 5),
    ([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 5),
    ([3, 14, 3, 14, 3, 14, 14, 3, 3, 14, 14, 14, 3, 14, 14, 3, 14, 14, 14, 3], 7),
    ([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 7),
    (
        [
            370,
            370,
            448,
            448,
            370,
            234,
            448,
            448,
            347,
            234,
            448,
            448,
            448,
            370,
            448,
            448,
            234,
            448,
            448,
            467,
            370,
            347,
            448,
            448,
            448,
            448,
            448,
            448,
            370,
            448,
            467,
            448,
            448,
            448,
            448,
            448,
            448,
            370,
            370,
            448,
            347,
            448,
            448,
            370,
            370,
            448,
            448,
            448,
            448,
            448,
            448,
            347,
            448,
            347,
            467,
            448,
            448,
            448,
            370,
            448,
            448,
            370,
            448,
            448,
            448,
            448,
            448,
            448,
            448,
            234,
            370,
            234,
            448,
            448,
            448,
            448,
            467,
            370,
            448,
            448,
            448,
            448,
            448,
        ],
        30,
    ),
]

sol = Solution()
for t, r in tests[:]:
    print(sol.minOperations(t) == r)
