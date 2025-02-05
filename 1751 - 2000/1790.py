class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        k = 0
        for i, x in enumerate(s1):
            if x != s2[i]:
                k += 1
        return k <= 2
