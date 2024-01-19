class Solution:
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
