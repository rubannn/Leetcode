class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        rank = list(range(n))
        rank.sort(key=lambda x: -score[x])
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = [None] * n
        for i in range(n):
            res[rank[i]] = medals[i] if i < 3 else f"{i+1}"
        return res
