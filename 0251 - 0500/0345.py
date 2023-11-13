class Solution:
    def reverseVowels(self, s: str) -> str:
        v = 'aeiouAEIOU'
        x, y = 0, len(s) - 1
        s = list(s)
        while x < y:
            while (x < y and s[x] not in v):
                x += 1
            while (x < y and s[y] not in v):
                y -= 1
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
        return ''.join(s)
