# equation (ax + by = 1) have solve if gcd(a, b) = 1
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        t = nums[0]
        for x in nums:
            t = gcd(t, x)
            if t == 1:
                return True
        return False
