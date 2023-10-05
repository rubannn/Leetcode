from math import floor
from collections import Counter

class Solution:
    # variant 1
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

    # variant 2
    def majorityElement2(self, nums: List[int]) -> int:
        dct = Counter(nums)
        t = floor(len(nums) / 2)
        return [x for x, y in dct.items() if y > t][0]
