def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix) - 1, len(matrix[0]) - 1
    while matrix[m][n] > target and m > 0:
        m -= 1
    if target > matrix[m][n] and m + 1 < len(matrix):
        m += 1
    while matrix[m][n] > target and n > 0:
        n -= 1
    return matrix[m][n] == target
