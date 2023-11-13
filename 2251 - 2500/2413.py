class Solution:
    # def smallestEvenMultiple(self, n: int) -> int:
    #     return n if n % 2 == 0 else 2 * n

    def smallestEvenMultiple(self, n: int) -> int:
        return (2 - int(n % 2 == 0)) * n
