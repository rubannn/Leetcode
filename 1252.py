class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matr = [[0 for _ in range(n)] for _ in range(m)]
        s = 0
        for r, c in indices:
            for t in range(n):
                matr[r][t] += 1
                s += (-1) ** (matr[r][t] % 2)
            for t in range(m):
                matr[t][c] += 1
                s += (-1) ** (matr[t][c] % 2)
        return abs(s)
