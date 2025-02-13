import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while len(nums) > 1:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x >= k:
                return count
            t = x * 2 + y
            heapq.heappush(nums, t)
            count += 1
        return count
