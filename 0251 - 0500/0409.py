from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dc = Counter(s)
        dc_odd = [x for x in dc.values() if x % 2 == 1]
        return sum(dc.values()) - len(dc_odd) + (1 if dc_odd else 0)
