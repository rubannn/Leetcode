from typing import List


class Solution:
    # variant 1
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n - 1, 0, -1):
            for j in range(n):
                mn = matrix[i][j]
                if j - 1 >= 0:
                    mn = min(matrix[i][j - 1], mn)
                if j + 1 < n:
                    mn = min(matrix[i][j + 1], mn)
                matrix[i - 1][j] += mn
        return min(matrix[0])

    # variant 2
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n - 1, 0, -1):
            for j in range(n):
                matrix[i - 1][j] += min(
                    matrix[i][j], matrix[i][max(j - 1, 0)], matrix[i][min(j + 1, n - 1)]
                )
        return min(matrix[0])
