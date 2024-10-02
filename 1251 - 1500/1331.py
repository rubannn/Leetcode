class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        rank = dict(zip(s, range(1, len(s) + 1)))
        return [rank[x] for x in arr]
