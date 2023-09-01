class Solution:
# variant 1
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

# variant 2
    def matrixSum(self, nums: List[List[int]]) -> int:
        for x in range(len(nums)):
            nums[x] = sorted(nums[x])[::-1]

        s, p, c = 0, len(nums[0]), 0
        for _ in range(p):
            mx = []
            for x in range(len(nums)):
                mx.append(nums[x][c])
            c += 1
            s += max(mx)
        return s
