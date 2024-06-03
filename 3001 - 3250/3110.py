class Solution:
    def scoreOfString(self, s: str) -> int:
        pred = s[0]
        res = 0
        for c in s:
            res += abs(ord(c) - ord(pred))
            pred = c
        return res
