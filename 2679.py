class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        s, p = 0, len(nums[0])
        for _ in range(p):
            mx = []
            for x in range(len(nums)):
                t = nums[x]
                cmx = max(t)
                t.remove(cmx)
                nums[x] = t
                mx.append(cmx)
            s += max(mx)
        return s
