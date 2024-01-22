class Solution:
    # variant 1 (9632 ms 15.4 MB)
    def findErrorNums(self, nums: list[int]) -> list[int]:
        for x in nums:
            if nums.count(x) == 2:
                return [x, len(nums) * (len(nums) + 1) // 2 - sum(nums) + x]

    # variant 2 (157 ms 18.6 MB)
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums_set = set()
        for x in nums:
            if x not in nums_set:
                nums_set.add(x)
            else:
                return [x, len(nums) * (len(nums) + 1) // 2 - sum(nums) + x]
