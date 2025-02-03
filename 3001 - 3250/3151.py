class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        res = True
        pred = nums[0]
        for x in nums[1:]:
            res = res and (x % 2 != pred % 2)
            pred = x
        return res
