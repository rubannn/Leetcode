class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while True:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
            if not ((0 <= x < m) and (0 <= y < n)):
                return False
