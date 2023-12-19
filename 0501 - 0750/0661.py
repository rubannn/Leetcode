from itertools import product
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        vectors = list(product((-1, 0, 1), (-1, 0, 1)))
        res = []
        for i in range(m):
            row = []
            for j in range(n):
                s, k = 0, 0
                for vi, vj in vectors:
                    if i + vi < 0 or j + vj < 0 or i + vi >= m or j + vj >= n:
                        continue
                    s += img[i + vi][j + vj]
                    k += 1
                row.append(s // k)
            res.append(row)
        return res
