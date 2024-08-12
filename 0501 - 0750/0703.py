from heapq import heappush, heappop


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hstack = []
        for el in nums:
            self.add(el)

    def add(self, val: int) -> int:
        heappush(self.hstack, val)
        if len(self.hstack) > self.k:
            heappop(self.hstack)
        return self.hstack[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
