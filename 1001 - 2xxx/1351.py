class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        k = 0
        for x in range(m - 1, -1 , -1):
            for y in range(n - 1, -1, -1):
                if grid[x][y] < 0:
                    k += 1
                else:
                    break
        return k
