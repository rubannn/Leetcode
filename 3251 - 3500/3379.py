from typing import List


class Solution:
    # variant 1
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = nums[:]
        n = len(nums)
        for i, x in enumerate(nums):
            res[i] = nums[(i + x) % n]
        return res

    # variant 2
    def constructTransformedArray2(self, nums: List[int]) -> List[int]:
        res = nums[:]
        n = len(nums)
        for i, x in enumerate(nums):
            p = i + x
            if p > n - 1:
                while p > n - 1:
                    p -= n
            elif p < 0:
                while p < 0:
                    p += n
            res[i] = nums[p]
        return res
