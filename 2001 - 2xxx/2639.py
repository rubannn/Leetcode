class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        grid = [[len(str(y)) for y in x] for x in zip(*grid)]
        return [max(x) for x in grid]
