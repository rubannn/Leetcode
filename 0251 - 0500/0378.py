class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        elems = dict()
        for row in matrix:
            for x in row:
                elems[x] = elems.get(x, 0) + 1
        elems = sorted([(x, y) for x, y in elems.items()], key=lambda t: t[0])
        t = i = 0
        while t < k:
            t += elems[i][1]
            i += 1
        return elems[i-1][0]
