def repeatedSubstringPattern(self, s: str) -> bool:
    n = len(s)
    for i in range(1, n):
        t = s[:i]
        if t * (n // len(t)) == s:
            return True
    return False
