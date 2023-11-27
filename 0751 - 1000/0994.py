from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        maps = []
        oranges = 0
        for _ in range(2):
            mp = []
            for i in range(n):
                row = []
                for j in range(m):
                    oranges += (grid[i][j] == 1)
                    row.append(grid[i][j])
                mp.append(row)
            maps.append(mp)

        minutes = 0
        level = 0
        while maps[0] != maps[1] or minutes == 0:
            level = (level + 1) % 2
            for i in range(n):
                for j in range(m):
                    if maps[(level + 1) % 2][i][j] == 2:
                        if i-1 >= 0 and maps[level][i-1][j] == 1:
                            oranges -= 1
                            maps[level][i-1][j] = 2
                        if i+1 < n and maps[level][i+1][j] == 1:
                            oranges -= 1
                            maps[level][i+1][j] = 2
                        if j-1 >= 0 and maps[level][i][j-1] == 1:
                            oranges -= 1
                            maps[level][i][j-1] = 2
                        if j+1 < m and maps[level][i][j+1] == 1:
                            oranges -= 1
                            maps[level][i][j+1] = 2
            minutes += 1
        return (minutes - 1) if oranges == 0 else -1




sol = Solution()
tests = [
    [[[2,1,1],[1,1,0],[0,1,1]], 4],
    [[[0,2]], 0],
    [[[2,1,1],[0,1,1],[1,0,1]], -1]
]
for grid, res in tests[:]:
    print(sol.orangesRotting(grid) == res)
