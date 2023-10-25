class Solution:
    def concatenatedBinary(self, n: int) -> int:
        b = ''.join(f'{d:0b}' for d in range(1, n+1))
        return int(b, 2) % (10**9 + 7)
