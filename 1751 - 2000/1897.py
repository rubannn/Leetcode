class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n, dc = len(words), dict()
        for w in words:
            for c in w:
                dc[c] = dc.get(c, 0) + 1
        for k in dc:
            if dc[k] % n != 0:
                return False
        return True
