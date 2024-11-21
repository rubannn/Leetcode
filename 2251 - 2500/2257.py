from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for a, b in walls:
            grid[a][b] = 100

        for a, b in guards:
            grid[a][b] = 100

        for a, b in guards:
            i, j = a, b
            while i - 1 >= 0 and grid[i - 1][j] < 100:
                i -= 1
                grid[i][j] = 1
            i, j = a, b
            while j - 1 >= 0 and grid[i][j - 1] < 100:
                j -= 1
                grid[i][j] = 1
            i, j = a, b
            while i + 1 < m and grid[i + 1][j] < 100:
                i += 1
                grid[i][j] = 1
            i, j = a, b
            while j + 1 < n and grid[i][j + 1] < 100:
                j += 1
                grid[i][j] = 1

        return sum(c == 0 for row in grid for c in row)


tests = [
    (4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]], 7),
    (3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]], 4),
]
sol = Solution()
for m, n, gg, ww, ans in tests[:]:
    print(sol.countUnguarded(m, n, gg, ww) == ans)
