from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last, res = 0, 0
        for row in bank:
            t = row.count("1")
            if t > 0:
                res += t * last
                last = t
        return res


tests = [(["011001", "000000", "010100", "001000"], 8), (["000", "111", "000"], 0)]

sol = Solution()
for b, ans in tests:
    print(sol.numberOfBeams(b) == ans)
