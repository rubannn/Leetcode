class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = j = 0
        pred_mx = -1
        while i < n:
            mx = mn = nums[i]
            bt = f"{mx:b}".count("1")
            j = i + 1
            while j < n and bt == f"{nums[j]:b}".count("1"):
                mx = max(nums[j], mx)
                mn = min(nums[j], mn)
                j += 1
            if pred_mx > mn:
                return False
            pred_mx = mx
            i = j
        return True


tests = [
    ([8, 4, 2, 30, 15], True),
    ([1, 2, 3, 4, 5], True),
    ([20, 16], False),
    ([136, 256, 10], False),
    ([75, 34, 30], False),
    ([174, 175, 234, 188], True),
    ([3, 16, 8, 4, 2], False),
]
sol = Solution()
for t, ans in tests[:]:
    print(sol.canSortArray(t) == ans)
