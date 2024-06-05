from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dc = Counter(words[0])
        for word in words:
            dc_w = Counter(word)
            for k in dc:
                dc[k] = min(dc[k], dc_w[k])
        res = []
        for k, v in dc.items():
            res += [k] * v
        return res
