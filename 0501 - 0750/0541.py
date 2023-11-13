class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        t = 0
        for i in range(0, len(s), k):
            if (t % 2 == 0):
                res.append(s[i:i+k][::-1])
            else:
                res.append(s[i:i+k])
            t += 1
        return ''.join(res)
