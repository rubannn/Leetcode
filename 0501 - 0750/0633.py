class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5) + 1):
            b2 = c - a**2
            if b2 >= 0:
                b = int(b2**0.5)
                if a**2 + b**2 == c:
                    return True
        return False
