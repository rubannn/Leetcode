class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        v = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        res = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    k = 4
                    for a, b in v:
                        if 0 <= x + a < n and 0 <= y + b < m:
                            k -= grid[x + a][y + b] == 1
                    res += k
        return res
