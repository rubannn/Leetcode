class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        for c in t:
            if s and s[0] == c:
                s = s[1:]
            if not s:
                return True
        return False
