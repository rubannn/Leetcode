class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        L_sum, R_sum = 0, sum(nums)
        if R_sum % 2 == 1:
            return 0
        res = 0
        for x in nums[:-1]:
            L_sum += x
            R_sum -= x
            res += (L_sum - R_sum) % 2 == 0
        return res
