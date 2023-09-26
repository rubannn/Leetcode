class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r, c = len(matrix), len(matrix[0])
        if r == 1 or c == 1:
            return True
        res = [set() for _ in range(r + c - 1)]
        for i in range(r):
            for j in range(c):
                res[i - j + c - 1].add(matrix[i][j])
        return all(len(x) == 1 for x in res)
