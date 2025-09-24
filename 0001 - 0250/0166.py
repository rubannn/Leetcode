class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = ("", "-")[(numerator < 0) ^ (denominator < 0)]
        numerator, denominator = abs(numerator), abs(denominator)

        ceil = numerator // denominator
        remainder = numerator % denominator
        result = f"{ceil}"
        pos_dict = dict()
        fraction = ""

        while remainder != 0:
            if remainder in pos_dict:
                start = pos_dict[remainder]
                non_period = fraction[:start]
                period = fraction[start:]
                return f"{sign}{result}.{non_period}({period})"

            pos_dict[remainder] = len(fraction)
            remainder *= 10
            digit = remainder // denominator
            remainder = remainder % denominator
            fraction += f"{digit}"

        if fraction:
            result += f".{fraction}"

        return f"{sign}{result}"


tests = [
    (1, 2, "0.5"),
    (2, 1, "2"),
    (4, 333, "0.(012)"),
    (1, 6, "0.1(6)"),
    (-50, 8, "-6.25"),
    (7, -12, "-0.58(3)"),
    (-22, -2, "11"),
]

sol = Solution()
for numerator, denominator, ans in tests[:]:
    print(sol.fractionToDecimal(numerator, denominator) == ans)
