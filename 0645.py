def findErrorNums(self, nums: list[int]) -> list[int]:
    for x in nums:
        if nums.count(x) == 2:
            return [x, len(nums)*(len(nums) + 1) // 2 - sum(nums) + x]
