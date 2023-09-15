class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = sum(list(set(nums)))
        return ones - (sum(nums) - ones) // 2
