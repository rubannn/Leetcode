from leetcode import *


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n in (2, 3, 5):
                return True
            elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n < 0 or n == 1:
                return False
            p, q, h = 7, 11, n**0.5
            while q <= h and (n % p != 0) and (n % q != 0):
                p, q = p + 6, q + 6
            if q <= h or p <= h and n % p == 0:
                return False
            return True

        p = [x for x in range(left, right + 1) if is_prime(x)]
        if len(p) < 2:
            return [-1, -1]

        res = p[:2]
        diff = res[1] - res[0]
        for i in range(len(p) - 1):
            if p[i + 1] - p[i] < diff:
                diff = p[i + 1] - p[i]
                res = [p[i], p[i + 1]]
        return res


tests = [([10, 19], [11, 13]), ([4, 6], [-1, -1]), ([19, 31], [29, 31])]

sol = Solution()
for arr, ans in tests[:]:
    print(sol.closestPrimes(*arr) == ans)
