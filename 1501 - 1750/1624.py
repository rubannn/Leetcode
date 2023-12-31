class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dc = dict()
        for i, c in enumerate(s):
            if dc.get(c, -1) == -1:
                dc[c] = [i, -1]
            else:
                dc[c] = [dc[c][0], i]
        res = max(y - x - 1 for x, y in dc.values())
        return (-1, res)[res >= 0]
