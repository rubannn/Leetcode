class Solution:
    # variant 1
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]

    # variant 2
    def maxProductDifference(self, nums: List[int]) -> int:
        mx1, mx2 = 0, 0
        mn1, mn2 = 10**5, 10**5
        for x in nums:
            if x > mx1:
                mx2 = mx1
                mx1 = x
            elif x > mx2:
                mx2 = x

            if x < mn1:
                mn2 = mn1
                mn1 = x
            elif x < mn2:
                mn2 = x

        return mx1 * mx2 - mn1 * mn2
