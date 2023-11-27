class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min = (sum(piles) + h - 1) // h # ceil(sum(piles) / h)
        k_max = max(piles)

        l, r = k_min, k_max + 1
        while l < r:
            k = (l + r) // 2
            t = sum((p + k - 1) // k for p in piles) # sum(ceil(p / k) for p in piles)
            if t <= h:
                r = k
            else: # t > h
                l = k + 1
        return l
