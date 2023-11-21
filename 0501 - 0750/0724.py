from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum, r_sum = 0, sum(nums[1:])
        for i in range(len(nums)-1):
            print(l_sum, r_sum)
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
            r_sum -= nums[i+1]
        if l_sum == r_sum:
            return len(nums) - 1
        return -1
