from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dc = Counter(s)
        for i, c in enumerate(s):
            if dc[c] == 1:
                return i
        return -1
