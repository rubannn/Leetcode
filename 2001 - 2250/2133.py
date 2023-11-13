class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
            n = len(matrix)
            s = n * (n + 1) // 2
            return all(sum(x) == s and len(set(x)) == n for x in matrix) and all(sum(x) == s and len(set(x)) == n for x in zip(*matrix))
