class Solution:
    def sortVowels(self, s: str) -> str:
        v = 'AEIOUaeiou'
        vv = sorted([c for c in s if c in v], key=lambda x: v.index(x))
        s = list(s)
        k = 0
        for i, c in enumerate(s):
            if c in v:
                  s[i] = vv[k]
                  k += 1
        return ''.join(s)
