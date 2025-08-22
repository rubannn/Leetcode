from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        a, b = [m, n], [-1, -1]
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    a = [min(a[0], x), min(a[1], y)]
                    b = [max(b[0], x), max(b[1], y)]

        return (b[0] - a[0] + 1) * (b[1] - a[1] + 1)
