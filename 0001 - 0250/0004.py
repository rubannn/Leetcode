class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i = j = 0
        nums = []
        while i < m or j < n:
            while i < m and (j == n or nums1[i] < nums2[j]):
                nums.append(nums1[i])
                i += 1
            while j < n and (i == m or nums1[i] >= nums2[j]):
                nums.append(nums2[j])
                j += 1
        index = (m + n) // 2
        if (m + n) % 2:
            return nums[index]
        return sum(nums[index - 1: index + 1]) / 2
