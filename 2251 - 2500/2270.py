class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        sum_l, sum_r = 0, sum(nums)
        for i in range(len(nums) - 1):
            x = nums[i]
            sum_l += x
            sum_r -= x
            if sum_l >= sum_r:
                res += 1
        return res
