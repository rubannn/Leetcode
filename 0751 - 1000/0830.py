class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        pred = s[0]
        L = R = cnt = 0
        for i, c in enumerate(s):
            if c == pred:
                R = i
                cnt += 1
            else:
                if cnt > 2:
                    res.append([L, R])
                cnt = 1
                L = R = i
            pred = c
        if cnt > 2:
            res.append([L, R])
        return res
