class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n - 1, 0, -1):
            for j in range(n):
                grid[i - 1][j] += min(grid[i][x] for x in range(n) if x != j)
        return min(grid[0])
