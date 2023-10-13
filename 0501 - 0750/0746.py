class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for x in range(2, len(cost)):
            cost[x] += min(cost[x-1], cost[x-2])
        return min(cost[-1], cost[-2])
