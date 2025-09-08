class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(x):
            return str(x).count("0") == 0

        for x in range(1, n + 1):
            if True == check(x) == check(n - x):
                return [x, n - x]
