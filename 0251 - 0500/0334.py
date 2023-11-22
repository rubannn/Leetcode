class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float("inf"), float("inf")
        for n in nums:
            first = min(first, n)
            if n > first:
                second = min(second, n)
            if n > second:
                return True
        return False
