class Solution:
    def minOperations(self, s: str) -> int:
        s0 = s1 = 0
        for i, c in enumerate(s):
            if i % 2 == 0:
                if c != "0":
                    s0 += 1
                else:
                    s1 += 1
            else:
                if c != "1":
                    s0 += 1
                else:
                    s1 += 1
        return min(s0, s1)
