from math import gcd, lcm
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = [nums[0]]
        for x in nums[1:]:
            y = stack[-1]
            if x == y and x != 1:
                continue
            if x != y and gcd(x, y) > 1:
                stack[-1] = lcm(x, y)
                while len(stack) > 1:
                    y = stack[-1]
                    x = stack[-2]
                    if gcd(x, y) > 1:
                        stack[-2] = lcm(x, y)
                        stack.pop()
                    else:
                        break
            else:
                stack.append(x)
        return stack


tests = [
    ([6, 4, 3, 2, 7, 6, 2], [12, 7, 6]),
    ([2, 2, 1, 1, 3, 3, 3], [2, 1, 1, 3]),
    ([287, 41, 49, 287, 899, 23, 23, 20677, 5, 825], [2009, 20677, 825]),
    ([1], [1]),
    ([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]),
]

sol = Solution()
for nums, ans in tests[:]:
    print(sol.replaceNonCoprimes(nums) == ans)
