from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = 0
        if n1 % 2 == 1:
            for x in nums2:
                res ^= x

        if n2 % 2 == 1:
            for x in nums1:
                res ^= x
        return res


sol = Solution()
tests = [([2, 1, 3], [10, 2, 5, 0], 13), ([1, 2], [3, 4], 0)]
for n1, n2, ans in tests[:]:
    print(sol.xorAllNums(n1, n2) == ans)
