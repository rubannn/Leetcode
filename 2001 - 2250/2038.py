class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        res = {'A':0, 'B':0}
        for c in range(1, len(colors) - 1):
            if colors[c-1: c+2] == 'AAA' or colors[c-1: c+2] == 'BBB':
                res[colors[c]] += 1
        return res['A'] > res['B']
