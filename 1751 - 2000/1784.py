class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones = [len(x) for x in s.split('0') if len(x) > 0]
        return len(ones) == 1
