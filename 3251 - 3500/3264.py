import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        q = []
        heapq.heapify(q)
        for i, item in enumerate(nums):
            heapq.heappush(q, (item, i))

        for _ in range(k):
            x = heapq.heappop(q)
            heapq.heappush(q, (x[0] * multiplier, x[1]))
        return [item[0] for item in sorted(q, key=lambda t: t[1])]
