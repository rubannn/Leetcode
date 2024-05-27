class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if sum(1 for t in nums if t >= x) == x:
                return x
        return -1
