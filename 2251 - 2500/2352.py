class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dc = dict()
        for i, row in enumerate(grid):
            dc[tuple(row)] = dc.get(tuple(row), {'rows': [], 'cols': []})
            dc[tuple(row)]['rows'] += [i]
        for i, row in enumerate(zip(*grid)):
            dc[tuple(row)] = dc.get(tuple(row), {'rows': [], 'cols': []})
            dc[tuple(row)]['cols'] += [i]
        res = 0
        for data in dc.values():
            row, col = len(data['rows']), len(data['cols'])
            if row > 0 and col > 0:
                res += row * col
        return res
