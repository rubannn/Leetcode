# https://oeis.org/A344389

from math import factorial as fact


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [1]
        for s in range(1, n + 1):
            dp.append(9*fact(9) // fact(10-s) + dp[-1])
        return dp[-1]
