class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = sorted([(x, y) for x, y in Counter(nums).items()], key=lambda x: (x[0] % 2, -x[1], x[0]))
        return nums[0][0] if nums[0][0] % 2 == 0 else -1
