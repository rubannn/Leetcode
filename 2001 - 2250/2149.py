from typing import List


class Solution:
    # variant 1 (1037 ms, 48.1 MB)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        plus, minus = [], []
        for x in nums:
            if x >= 0:
                plus += [x]
            else:
                minus += [x]
        res = []
        for x, y in zip(plus, minus):
            res += [x, y]
        return res

    # variant 2 (996 ms, 47.3 MB)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        a, b = 0, 1
        for x in nums:
            if x > 0:
                res[a] = x
                a += 2
            else:
                res[b] = x
                b += 2
        return res
