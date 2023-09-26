class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = set(range(1, n+1)) - set(nums)
        return list(res)
