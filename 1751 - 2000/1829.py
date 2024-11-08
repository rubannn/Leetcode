class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        mx, t = 2**maximumBit - 1, 0
        for x in nums:
            t = t ^ x
            res.append(t ^ mx)
        return res[::-1]


tests = [
    ([0, 1, 1, 3], 2, [0, 3, 2, 3]),
    ([2, 3, 4, 7], 3, [5, 2, 6, 5]),
    ([0, 1, 2, 2, 5, 7], 3, [4, 3, 6, 4, 6, 7]),
]
sol = Solution()
for t, m, ans in tests[:]:
    print(sol.getMaximumXor(t, m) == ans)
