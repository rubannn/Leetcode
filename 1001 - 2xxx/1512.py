from math import comb


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        cmb = [comb(nums.count(x), 2) for x in set(nums)]
        return sum(cmb)
