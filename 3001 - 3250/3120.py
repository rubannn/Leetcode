from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        dc = defaultdict(set)
        for c in word:
            dc[c.lower()].add(c)
        return sum(1 for k in dc if len(dc[k]) == 2)
