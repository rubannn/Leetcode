class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        res = 0
        for i in range(n // 2):
            if s[i] in "aeiouAEIOU":
                res += 1
            if s[n - i - 1] in "aeiouAEIOU":
                res -= 1
        return res == 0
