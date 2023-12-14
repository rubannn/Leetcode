class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_sums, col_sums = [], []
        for row in grid:
            row_sums.append(sum(row))

        for row in zip(*grid):
            col_sums.append(sum(row))
        m, n = len(grid), len(grid[0])
        s = m + n
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2*row_sums[i] + 2*col_sums[j] - s
        return grid
