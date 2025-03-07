from leetcode import *


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right, center = [], [], []
        for x in nums:
            if x < pivot:
                left += [x]
            elif x > pivot:
                right += [x]
            else:
                center += [x]

        return left + center + right


tests = [
    ([9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14]),
    ([-3, 4, 3, 2], 2, [-3, 2, 4, 3]),
]

sol = Solution()
for arr, p, ans in tests[:]:
    print(sol.pivotArray(arr, p) == ans)
