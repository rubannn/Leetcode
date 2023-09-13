class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(m):
            for y in range(n):
                t = 0
                ql, qr = max(x-k, 0), min(m, x + k + 1)
                wl, wr = max(y-k, 0), min(n, y + k + 1)
                for q in range(ql, qr):
                    for w in range(wl, wr):
                        t += mat[q][w]
                res[x][y] = t
        return res
