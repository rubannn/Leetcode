class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        sa, sb = set(nums1), set(nums2)
        return [[c for c in sa - sb], [c for c in sb - sa]]
