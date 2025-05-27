class Solution:
    # viriant 1: O(1) time complexity
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        k = n // m
        sum_div = m * k * (k + 1) // 2
        return total_sum - 2 * sum_div

    # variant 2: O(n/m) time complexity
    def differenceOfSums2(self, n: int, m: int) -> int:
        sum_div = sum(x for x in range(m, n + 1, m))
        return sum(range(1, n + 1)) - 2 * sum_div
