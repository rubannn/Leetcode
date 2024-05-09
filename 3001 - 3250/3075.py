class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i, h in enumerate(happiness[:k]):
            h -= i
            res += max(h, 0)
        return res
