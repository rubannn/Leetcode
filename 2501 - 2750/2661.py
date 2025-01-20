from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        map = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}
        rows = [0] * m
        cols = [0] * n

        for x in range(len(arr)):
            a, b = map[arr[x]]
            rows[a] += 1
            cols[b] += 1
            if rows[a] == n or cols[b] == m:
                return x


sol = Solution()
tests = [
    ([1, 3, 4, 2], [[1, 4], [2, 3]], 2),
    ([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]], 3),
]
for n1, n2, ans in tests[:]:
    print(sol.firstCompleteIndex(n1, n2) == ans)
