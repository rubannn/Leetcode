class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = [1]
        for i in range(1, len(nums)):
            pr.append(nums[i-1] * pr[-1])

        rp = 1
        for i in range(len(nums)-1, -1, -1):
            pr[i] *= rp
            rp *= nums[i]
        return pr
