from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        minors1 = version1.split(".")
        minors2 = version2.split(".")

        for a, b in zip_longest(minors1, minors2, fillvalue=0):
            if int(a) < int(b):
                return -1
            if int(a) > int(b):
                return 1
        return 0


tests = [
    ("1.0.1", "1", 1),
    ("0.1", "1.1", -1),
    ("1.0", "1.0.0", 0),
    ("1.01", "1.001", 0),
]

sol = Solution()
for v1, v2, ans in tests:
    print(sol.compareVersion(v1, v2) == ans)
