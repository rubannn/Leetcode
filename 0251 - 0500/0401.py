class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                b = f'{h:b}:{m:b}'
                if b.count('1') == turnedOn:
                    res.append(f'{h}:{m:02d}')
        return res
