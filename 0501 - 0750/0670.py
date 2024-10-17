class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(digit): i for i, digit in enumerate(digits)}

        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int("".join(digits))
        return num


sol = Solution()
tests = [(2736, 7236), (9973, 9973), (3979, 9973), (1032, 3012)]
for a, b in tests:
    print(sol.maximumSwap(a) == b)
