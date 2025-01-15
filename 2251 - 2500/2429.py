class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits = f"{num2:b}".count("1")
        res = []
        for c in f"{num1:b}":
            if bits > 0 and c == "1":
                res += ["1"]
                bits -= 1
            else:
                res += ["0"]

        i = len(res) - 1
        while bits > 0:
            if i < 0:
                res = ["1"] + res
                bits -= 1
            else:
                if res[i] == "0" and bits > 0:
                    res[i] = "1"
                    bits -= 1
            i -= 1
        return int("".join(res), 2)


sol = Solution()
tests = [(3, 5, 3), (1, 12, 3), (25, 72, 24), (65, 84, 67)]
for n1, n2, ans in tests[:]:
    print(sol.minimizeXor(n1, n2) == ans)
