def spiralOrder(matrix: list[list[int]]) -> list[int]:
    x = y = p = 0
    v = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m, n = len(matrix), len(matrix[0])
    k = m * n
    res = []
    while k > 0:
        res.append(matrix[x][y])
        matrix[x][y] = '#'
        if not ((0 <= x + v[p][0] < m) and (0 <= y + v[p][1] < n)
                and (matrix[x + v[p][0]][y + v[p][1]] != '#')):
            p = (p + 1) % 4
        x += v[p][0]
        y += v[p][1]
        k -= 1
    return res


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralOrder(m) == r)

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
r = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(spiralOrder(m) == r)
