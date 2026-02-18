class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = n & 1
        n >>= 1
        while n > 0:
            current_bit = n & 1
            if current_bit == prev_bit:
                return False
            prev_bit = current_bit
            n >>= 1

        return True

sol = Solution()
for t in [5, 7, 11, 10, 3]:
    print(f"{t} -> {sol.hasAlternatingBits(t)}")
