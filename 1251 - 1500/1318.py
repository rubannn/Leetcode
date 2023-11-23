class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = f'{a:032b}'
        b = f'{b:032b}'
        c = f'{c:032b}'
        count = 0
        for i in range(len(c)):
            if c[i] == '1':
                count += (a[i] == b[i] == '0')
            else:
                count += (a[i] == '1') + (b[i] == '1')
        return count


sol = Solution()
tests = [
    [[2, 6, 5], 3],
    [[4, 2, 7], 1],
    [[1, 2, 3], 0],
    [[7, 7, 7], 0]
]

for nums, ans in tests:
    x, y, z = nums
    print(sol.minFlips(x, y, z) == ans)
