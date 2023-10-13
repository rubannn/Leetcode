class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2[::-1], num1[::-1]
        else:
            num1, num2 = num1[::-1], num2[::-1]
        sums = []
        for i, x in enumerate(num2):
            s = ''
            v, rest = 0, 0
            for y in num1:
                v = int(x) * int(y) + rest
                s += str(v % 10)
                rest = v // 10
            if rest > 0:
                s += str(rest)
            sums.append('0'*i + s)

        p = ''
        rest, n = 0, len(sums[-1])
        for i in range(n):
            t = rest
            for s in sums:
                if i < len(s):
                    t += int(s[i])
            p = str(t % 10) + p
            rest = t // 10
        if rest > 0:
            p = str(rest) + p
        return '0' if '0' * len(p) == p else p
