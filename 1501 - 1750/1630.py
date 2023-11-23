class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for x, y in zip(l, r):
            arr = sorted(nums[x : y+1])
            n, d = len(arr), arr[-1] - arr[-2]
            res.append(2 * sum(arr) == (arr[0] + arr[-1]) * n == 2 * arr[0] * n + d * (n-1) * n and arr[0] - arr[1] == arr[-2] - arr[-1])
        return res
