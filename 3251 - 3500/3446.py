from collections import defaultdict
from typing import List
from icecream import ic

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        top = defaultdict(list)
        bottom = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i < j:
                    top[j - i].append(grid[i][j])
                else:
                    bottom[i - j].append(grid[i][j])

        for k in top:
            top[k] = sorted(top[k])
        for k in bottom:
            bottom[k] = sorted(bottom[k])[::-1]

        for i in range(n):
            for j in range(n):
                if i < j:
                    grid[i][j] = top[j - i][0]
                    top[j - i] = top[j - i][1:]
                else:
                    grid[i][j] = bottom[i - j][0]
                    bottom[i - j] = bottom[i - j][1:]

        return grid

    def sortMatrix2(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diags = defaultdict(list)
        for i in range(n):
            for j in range(n):
                key = i < j
                num = abs(i - j)
                diags[(key, num)].append(grid[i][j])

        for k in diags:
            diags[k] = sorted(diags[k], reverse=not k[0])

        for i in range(n):
            for j in range(n):
                key = i < j
                num = abs(i - j)
                grid[i][j] = diags[(key, num)][0]
                diags[(key, num)] = diags[(key, num)][1:]

        return grid


tests = (
    ([[1, 7, 3], [9, 8, 2], [4, 5, 6]], [[8, 2, 3], [9, 6, 7], [4, 5, 1]]),
    ([[0, 1], [1, 2]], [[2, 1], [1, 0]]),
    ([[3]], [[3]]),
)

sol = Solution()
for t, ans in tests:
    print(sol.sortMatrix2(t) == ans)
