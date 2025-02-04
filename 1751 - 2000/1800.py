class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        pred = nums[0]
        mx = res = pred
        for x in nums[1:]:
            if x > pred:
                res += x
            else:
                mx = max(mx, res)
                res = x
            pred = x
        return max(mx, res)
