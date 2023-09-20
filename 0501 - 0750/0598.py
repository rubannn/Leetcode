class Solution:
    # variant 1 (Time = 294 ms; Memory = 18.5 MB)
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rows, cols = [0] * m, [0] * n
        for x, y in ops:
            for t in range(x):
                rows[t] += 1
            for t in range(y):
                cols[t] += 1
        return rows.count(rows[0]) * cols.count(rows[0])

    # variant 2 (Time = 75 ms; Memory = 18.3 MB)
    def maxCount2(self, m: int, n: int, ops: List[List[int]]) -> int:
        r, c = m, n
        for x, y in ops:
            r = min(r, x)
            c = min(c, y)
        return r * c
