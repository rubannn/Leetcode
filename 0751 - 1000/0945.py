from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        pred = nums[0]
        res = 0
        for x in nums[1:]:
            ds = 0
            if pred >= x:
                ds = pred - x + 1
            pred = x + ds
            res += ds
        return res


tests = [([1, 2, 2], 1), ([3, 2, 1, 2, 1, 7], 6)]
sol = Solution()
for arr, ans in tests:
    print(sol.minIncrementForUnique(arr), ans)
