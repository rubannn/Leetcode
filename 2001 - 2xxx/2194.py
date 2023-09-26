class Solution:
    def cellsInRange(self, s: str) -> List[str]:
            s = s.split(':')
            res = []
            for c in range(ord(s[0][0]), ord(s[1][0])+1):
                for d in range(ord(s[0][1]), ord(s[1][1])+1):
                    res.append(f'{chr(c)}{chr(d)}')
            return res
