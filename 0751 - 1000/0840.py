class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nums = set(range(1, 10))

        def check(mt):
            all = set().union(*mt) == nums
            if all:
                rows = list(set(sum(row) for row in mt))
                cols = list(set(sum(row) for row in list(zip(*mt))))
                d1 = sum([mt[0][0], mt[1][1], mt[2][2]])
                d2 = sum([mt[0][2], mt[1][1], mt[2][0]])
                return (
                    len(rows) == len(cols) == 1 and rows[0] == cols[0] == d1 == d2 == 15
                )
            else:
                return 0

        m, n = len(grid), len(grid[0])
        res = 0
        for x in range(m - 2):
            for y in range(n - 2):
                if 0 < grid[x][y] < 10:
                    submt = [row[y : y + 3] for row in grid[x : x + 3]]
                    res += check(submt)
        return res
