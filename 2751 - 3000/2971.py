class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        p, i = sum(nums), 0
        for x in nums:
            if p > 2 * x:
                return p
            p -= x
        return -1
