from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a, n = 0, len(nums)
        res = []
        while a < n:
            b = a + 1
            while b < n and nums[b] - nums[b - 1] == 1:
                b += 1

            if (b - 1 < n) and (a < b - 1):
                res.append(f"{nums[a]}->{nums[b-1]}")
            else:
                res.append(f"{nums[a]}")
            a = b
        return res
