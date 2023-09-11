def generateMatrix(n: int) -> list[list[int]]:
    v = ((0, 1), (1, 0), (0, -1), (-1, 0))
    res = [[0 for _ in range(n)] for _ in range(n)]
    x = y = 0
    p, k = 0, 1
    while k <= n ** 2:
        res[x][y] = k
        if not ((0 <= x + v[p][0] < n) and (0 <= y + v[p][1] < n)
                and (res[x + v[p][0]][y + v[p][1]] == 0)):
            p = (p + 1) % 4
        x += v[p][0]
        y += v[p][1]
        k += 1
    return res


n = 3
r = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(generateMatrix(n) == r)

n = 1
r = [[1]]
print(generateMatrix(n) == r)
