class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        s, g = dict(), dict()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1

        for k in s.keys():
            if k in g:
                b += min(s[k], g[k])
        return f"{a}A{b}B"
