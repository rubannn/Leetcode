from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n in (2, 3, 5, 7):
                return True
            elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n < 0 or n == 1:
                return False
            d = 7
            while d <= n**0.5:
                if n % d == 0:
                    return False
                d += 2
            return True

        prime = [x for x in range(max(nums)) if is_prime(x)]
        for i in range(len(nums) - 2, -1, -1):
            p = 0
            t = nums[i]
            while nums[i] >= nums[i + 1] and p < len(prime) and prime[p] < t:
                nums[i] = t - prime[p]
                p += 1

        return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))


tests = [
    ([4, 9, 6, 10], True),
    ([6, 8, 11, 12], True),
    ([5, 8, 3], False),
    ([2, 2], False),
]

sol = Solution()
for arr, ans in tests[:]:
    print(sol.primeSubOperation(arr) == ans)
