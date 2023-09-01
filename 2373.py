class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        mt = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                mt[j - 1][i - 1] = max(max(grid[j-1][i-1:i+2]), max(grid[j][i-1:i+2]), max(grid[j+1][i-1:i+2]))
        return mt
