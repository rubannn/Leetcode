class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nm, mx = dict(), [nums[0], 1]
        for i in range(len(nums)):
            if nm.get(nums[i]):
                nm[nums[i]] += 1
                if mx[1] < nm[nums[i]]:
                    mx = [nums[i], nm[nums[i]]]
            else:
                nm[nums[i]] = 1
        return mx[0]
