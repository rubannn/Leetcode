class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        divs = 0
        for i in range(1, int(a ** 0.5) + 1) :
            if (a % i == 0):
                if (b % i == 0):
                    divs += 1
                if (b % (a // i) == 0) and (a // i != i):
                    divs += 1
        return divs
