import re, math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        x, y = 0, 1
        pattern = r"[+-]?\d+/\d+"
        fracs = re.findall(pattern, expression)
        for f in fracs:
            a, b = map(int, f.split("/"))
            x, y = x * b + a * y, b * y
        _gcd = math.gcd(x, y)
        x, y = x // _gcd, y // _gcd
        return f"{x}/{y}"


tests = [("-1/2+1/2", "0/1"), ("-1/2+1/2+1/3", "1/3"), ("1/3-1/2", "-1/6")]
sol = Solution()

for inp, out in tests:
    print(sol.fractionAddition(inp) == out)
