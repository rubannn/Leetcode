class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for x in range(1, m):
            grid[x][0] = grid[x-1][0] + grid[x][0]
        for y in range(1, n):
            grid[0][y] = grid[0][y-1] + grid[0][y]

        for x in range(1, m):
            for y in range(1, n):
                grid[x][y] = min(grid[x-1][y], grid[x][y-1]) + grid[x][y]
        return grid[m-1][n-1]
