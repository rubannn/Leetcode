class Solution:
    # def smallestEvenMultiple(self, n: int) -> int:
    #     return n if n % 2 == 0 else 2 * n

    # variant 1
    def smallestEvenMultiple(self, n: int) -> int:
        return (2 - int(n % 2 == 0)) * n

    # variant 2
    def smallestEvenMultiple(self, n: int) -> int:
        return (n, 2 * n)[n % 2]
