class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for x in range(low, high + 1):
            n = len(f"{x}")
            if n % 2 == 0:
                p1 = f"{x}"[: n // 2]
                p2 = f"{x}"[n // 2 :]
                if sum(map(int, list(p1))) == sum(map(int, list(p2))):
                    count += 1
        return count
