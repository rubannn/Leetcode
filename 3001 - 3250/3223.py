class Solution:
    def minimumLength(self, s: str) -> int:
        dc = Counter(s)
        return sum(2 - (x & 1) for x in dc.values())
