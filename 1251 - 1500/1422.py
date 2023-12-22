class Solution:
    def maxScore(self, s: str) -> int:
        mx = tmp = (s[0] == "0") + s[1:].count("1")
        for i in range(1, len(s) - 1):
            tmp += 1 if s[i] == "0" else -1
            mx = max(mx, tmp)
        return mx
