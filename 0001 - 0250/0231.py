class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     return (n and (not (n & (n - 1))))

    def isPowerOfTwo(self, n: int) -> bool:
        while n % 2 == 0 and n != 0:
            n //= 2
        return n == 1
