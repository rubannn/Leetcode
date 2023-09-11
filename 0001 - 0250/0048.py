def rotate(self, matrix: list[list[int]]) -> None:
    n = len(matrix)
    for x in range(n // 2):
        for y in range(x, n - x - 1):
            t = matrix[y][x]
            matrix[y][x] = matrix[n-1-x][y]
            matrix[n-1-x][y] = matrix[n-1-y][n-1-x]
            matrix[n-1-y][n-1-x] = matrix[x][n-1-y]
            matrix[x][n-1-y] = t
