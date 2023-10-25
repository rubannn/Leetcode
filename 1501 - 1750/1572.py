class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = sum(mat[i][i] + mat[i][n-i-1] for i in range(n))
        return s - (mat[n//2][n//2] if n % 2 else 0)
