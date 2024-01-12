from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        v = [(1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1)]
        n, m = len(grid), len(grid[0])
        check = 0
        for i in range(n):
            for j in range(m):
                for q, w in v:
                    if (
                        0 <= i + q < n
                        and 0 <= j + w < m
                        and abs(grid[i][j] - grid[i + q][j + w]) == 1
                    ):
                        check += 1
        return check == n * m * 2 - 2


tests = [
    (
        [
            [0, 11, 16, 5, 20],
            [17, 4, 19, 10, 15],
            [12, 1, 8, 21, 6],
            [3, 18, 23, 14, 9],
            [24, 13, 2, 7, 22],
        ],
        True,
    ),
    ([[0, 3, 6], [5, 8, 1], [2, 7, 4]], False),
    (
        [
            [0, 13, 1, 7, 20],
            [3, 8, 19, 12, 15],
            [18, 2, 14, 21, 6],
            [9, 4, 23, 16, 11],
            [24, 17, 10, 5, 22],
        ],
        False,
    ),
    (
        [
            [0, 3, 6, 9, 18, 35],
            [7, 10, 1, 4, 29, 20],
            [2, 5, 8, 19, 34, 16],
            [11, 24, 13, 30, 21, 28],
            [14, 31, 26, 23, 17, 33],
            [25, 12, 15, 32, 27, 22],
        ],
        False,
    ),
    (
        [
            [24, 11, 22, 17, 4],
            [21, 16, 5, 12, 9],
            [6, 23, 10, 3, 18],
            [15, 20, 1, 8, 13],
            [0, 7, 14, 19, 2],
        ],
        False,
    ),
]

sol = Solution()
for t, ans in tests[:]:
    print(sol.checkValidGrid(t) == ans)
