class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mn = area
        res = []
        for a in range(1, int(area ** .5) + 1):
            if area % a == 0:
                b = area // a
                if abs(a - b) < mn:
                    mn = abs(a - b)
                    res = [a, b]
        return sorted(res, reverse=True)
