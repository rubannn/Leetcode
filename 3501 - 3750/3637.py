class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        a, n = 0, len(nums)
        while a < n and a + 1 < n and nums[a] < nums[a + 1]:
            a += 1
        b = a
        while b < n and b + 1 < n and nums[b] > nums[b + 1]:
            b += 1
        c = b
        while c < n and c + 1 < n and nums[c] < nums[c + 1]:
            c += 1
        return 0 < a < b < c < n and n - c == 1
