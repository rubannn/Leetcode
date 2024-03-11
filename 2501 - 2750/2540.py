class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        mn = set(nums1) & set(nums2)
        return min(mn) if mn else -1
