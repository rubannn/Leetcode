class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def realstr(x):
            res = []
            for c in x:
                if c != '#':
                    res.append(c)
                elif res:
                    res.pop()
            return res

        return realstr(s) == realstr(t)
