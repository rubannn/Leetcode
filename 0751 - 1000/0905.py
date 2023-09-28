class Solution:
    # variant 1
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)

    # variant 1
    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        return [x for k in (0, 1) for x in nums if x % 2 == k]
