from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        dc = Counter(t)
        for c in s:
            dc[c] = dc.get(c, 0) - 1
        return sum(x for x in dc.values() if x > 0)

    def minSteps2(self, s, t):
        dc = Counter(t)
        res = 0
        for c in s:
            if dc.get(c, 0) > 0:
                dc[c] -= 1
            else:
                res += 1
        return res
