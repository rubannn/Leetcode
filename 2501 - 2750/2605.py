class Solution:
    # variant 1 - 62 ms 17.3 MB
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1) & set(nums2)
        if intersection:
            res = [min(intersection)]
        else:
            res = sorted([min(nums1), min(nums2)])
        return int("".join(map(str, res)))

    # variant 2 - 37 ms 17.1 MB
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        m1, m2 = min(nums1), min(nums2)
        s = set(nums1) & set(nums2)
        if s:
            return min(s)
        else:
            return m2 * 10 + m1 if m1 > m2 else m1 * 10 + m2
