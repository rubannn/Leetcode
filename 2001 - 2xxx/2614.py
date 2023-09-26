class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n in (2, 3, 5, 7): return True
            elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n < 0 or n == 1: return False
            d = 7
            while d <= n**.5:
                if n % d == 0: return False
                d += 2
            return True

        n = len(nums)
        diag = [nums[i][i] for i in range(n)] + [nums[i][n-i-1] for i in range(n)]
        diag = [x for x in diag if is_prime(x)]
        return max(diag) if diag else 0
