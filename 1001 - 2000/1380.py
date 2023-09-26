class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        a = {min(x) for x in matrix}
        b = {max(x) for x in zip(*matrix)}
        return list(a & b)
