class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s1, s2 = set(), set()
        res = []
        for i, c in enumerate(arr):
            if c in s1:
                s2.add(c)
            else:
                s1.add(c)
                res.append((c, i))
        s1 = s1 - s2

        for a, b in res:
            if a in s1:
                k -= 1
                if k == 0:
                    return a
        return ""
