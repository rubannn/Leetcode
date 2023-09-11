def nthUglyNumber(self, n: int) -> int:
    res = []
    for a in range(50):
        for b in range(25):
            for c in range(15):
                res.append(2**a * 3**b * 5**c)
    return sorted(res)[n - 1]
