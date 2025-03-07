from leetcode import *


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        order_nums = [(i, v) for i, v in enumerate(nums)]
        order_nums = sorted(order_nums, key=lambda x: (x[1] == 0, x[0]))
        return [x[1] for x in order_nums]


tests = [([1, 2, 2, 1, 1, 0], [1, 4, 2, 0, 0, 0]), ([0, 1], [1, 0])]

sol = Solution()
for arr, ans in tests[:]:
    print(sol.applyOperations(arr), ans)
