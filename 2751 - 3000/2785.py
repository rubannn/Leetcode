class Solution:
    def sortVowels(self, s: str) -> str:
        v = "AEIOUaeiou"
        vv = sorted([c for c in s if c in v], key=lambda x: v.index(x))
        s = list(s)
        k = 0
        for i, c in enumerate(s):
            if c in v:
                s[i] = vv[k]
                k += 1
        return "".join(s)

    def sortVowels2(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        v = sorted([c for c in s if c in vowels], reverse=True)
        sn = ""
        for c in s:
            if c in vowels:
                sn += v.pop()
            else:
                sn += c
        return sn
