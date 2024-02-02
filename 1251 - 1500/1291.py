from typing import List


class Solution:
    # variant 1
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        base = "123456789"
        d = len(str(low))
        s = base.index(str(low)[0])
        x = int(base[s : s + d])
        while x < low and d < 10:
            s += 1
            if s + d > 9:
                s = 0
                d += 1
            x = int(base[s : s + d])
        if x < low:
            return []
        res = []
        while x <= high and d < 10:
            res.append(x)
            s += 1
            if s + d > 9:
                s = 0
                d += 1
            x = int(base[s : s + d])
        return res

    # variant 2
    def sequentialDigits2(self, low: int, high: int) -> List[int]:
        base = "123456789"
        s, d = 0, 2
        res = []
        while d < 10:
            x = int(base[s : s + d])
            if low <= x <= high:
                res.append(x)
            s += 1
            if s + d > 9:
                s = 0
                d += 1
        return res


tests = [
    (
        10,
        1000000000,
        [
            12,
            23,
            34,
            45,
            56,
            67,
            78,
            89,
            123,
            234,
            345,
            456,
            567,
            678,
            789,
            1234,
            2345,
            3456,
            4567,
            5678,
            6789,
            12345,
            23456,
            34567,
            45678,
            56789,
            123456,
            234567,
            345678,
            456789,
            1234567,
            2345678,
            3456789,
            12345678,
            23456789,
            123456789,
        ],
    ),
    (100, 300, [123, 234]),
    (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
    (58, 155, [67, 78, 89, 123]),
    (8511, 23553, [12345, 23456]),
    (178546104, 812704742, []),
]
sol = Solution()
for a, b, c in tests[:]:
    # print(sol.sequentialDigits(a, b) == c)
    print(sol.sequentialDigits2(a, b) == c)
