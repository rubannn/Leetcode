class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        pred = words[-1]
        res = True
        for w in words:
            res = res and (pred[-1] == w[0])
            pred = w
        return res
