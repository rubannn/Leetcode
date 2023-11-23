class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        L, R = 0, len(nums) - 1
        ans = 0
        while L < R:
            if nums[L] + nums[R] == k:
                ans += 1
                L += 1
                R -= 1
            elif nums[L] + nums[R] > k:
                R -= 1
            else:
                L += 1
        return ans
