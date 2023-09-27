class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def erase_island(r, c, grid):
            if (r < 0 or r > len(grid)-1) or (c < 0 or c > len(grid[0])-1)\
                or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            erase_island(r + 1, c, grid)
            erase_island(r - 1, c, grid)
            erase_island(r, c + 1, grid)
            erase_island(r, c - 1, grid)

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    res += 1
                    erase_island(x, y, grid)
        return res
