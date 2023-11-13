def matrixSumQueries(n: int, queries: list[list[int]]) -> int:
    rows, cols = [1] * n, [1] * n
    r, c, s = n, n, 0
    for t, i, v in queries[::-1]:
        if t == 0 and rows[i]:
            s += v * c
            r -= 1
            rows[i] = 0
        elif t == 1 and cols[i]:
            s += v * r
            c -= 1
            cols[i] = 0
    return s


n = 3
queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]
res = 23
print(matrixSumQueries(n, queries) == res)

n = 3
queries = [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]
res = 17
print(matrixSumQueries(n, queries) == res)
