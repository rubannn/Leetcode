class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        tmp = [y for x in grid for y in x]
        k = k % len(tmp)
        tmp = tmp[-k:] + tmp[:-k]
        return [tmp[i * c: (i + 1) * c] for i in range(r)]
