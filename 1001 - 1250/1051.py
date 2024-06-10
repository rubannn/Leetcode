class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        for a, b in zip(heights, sorted(heights)):
            if a != b:
                res += 1
        return res
