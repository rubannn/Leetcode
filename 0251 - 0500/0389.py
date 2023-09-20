class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = {c: t.count(c) for c in set(t)}
        for c in s:
            diff[c] -= 1
        return [c for c in diff if diff[c] > 0][0]
