from functools import cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        mod = 10**9 + 7
        variant = ((0, 1), (1, 0), (0, -1), (-1, 0))

        @cache
        def move(x, y, path):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            if path <= 0:
                return 0
            count = 0
            for i, j in variant:
                count = (count + move(x + i, y + j, path - 1)) % mod
            return count

        return move(startRow, startColumn, maxMove)
